import pygame
import sys

# تهيئة مكتبة Pygame
pygame.init()

# إعداد نافذة العرض
width, height = 1540, 880
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Rectangle - Fixed Collision")

bg_color = (0, 0, 0)

def cond(p, p2):
    """دالة فحص التصادم بين مستطيلين"""
    return p.x < p2.x + p2.width and p2.x < p.x + p.width and p.y < p2.y + p2.height and p2.y < p.y + p.height

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.n = 0  # القوة أو الزخم
        self.dr = 0 # الاتجاه (1 لليمين، -1 لليسار)
        self.color = color

    def draw(self, surface):
        """هذه الدالة مسؤولة فقط عن رسم اللاعب"""
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def update(self, other_player, screen_width):
        """
        هذه الدالة مسؤولة عن تحديث حالة اللاعب (الحركة والتصادم).
        هي الحل لمشكلة التخطي.
        """
        if self.n > 0:
            # نحدد اتجاه الحركة كخطوة واحدة (1 أو -1)
            step = 1 if self.dr > 0 else -1
            
            # نتحرك لمسافة القوة 'n' ولكن خطوة بخطوة
            for _ in range(int(self.n)):
                self.x += step

                # فحص الاصطدام باللاعب الآخر بعد كل خطوة صغيرة
                if cond(self, other_player):
                    # حدث تصادم!
                    # 1. نتراجع خطوة للخلف لمنع التداخل
                    self.x -= step
                    
                    # 2. ننقل القوة والاتجاه إلى اللاعب الآخر
                    other_player.dr = self.dr
                    other_player.n = self.n
                    
                    # 3. نوقف اللاعب الحالي
                    self.n =0      
                    # 4. نخرج من الدالة لأن التصادم حدث
                    return

                # فحص الاصطدام بحدود الشاشة
                if self.x <= 0 or self.x >= screen_width - self.width:
                    # نعكس الاتجاه
                    self.dr *= -1
                    # نمنع الخروج من الشاشة
                    self.x = max(0, min(self.x, screen_width - self.width))
                    # نوقف الحركة بعد الاصطدام بالجدار
                    break
            
            # إذا لم يحدث تصادم، نقلل القوة (احتكاك)
            if self.n > 0:
                self.n -= 0.5
                if self.n < 0:
                    self.n = 0

# إنشاء اللاعبين والأرضية
player1 = Player(50, (height / 2) - 50, 50, 50, (255, 255, 255))
player2 = Player(-50, (height / 2) - 50, 50, 50, (255, 0, 0))
ard = Player(0, height / 2, width, 20, (150, 150, 150))

# حلقة اللعبة الرئيسية
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # إعطاء اللاعب الأول قوة دفع كبيرة عند الضغط على المفاتيح
            if event.key == pygame.K_d: # غيرت المفتاح إلى D (يمين)
                player1.n = 100 # يمكنك وضع أي قوة هنا ولن تحدث مشكلة
                player1.dr = 1
            if event.key == pygame.K_a: # غيرت المفتاح إلى A (يسار)
                player1.n = 100
                player1.dr = -1
    
    # --- قسم التحديث ---
    # تحديث حالة كل لاعب قبل الرسم
    player1.update(player2, width)
    player2.update(player1, width) # يجب تحديث اللاعب الثاني أيضاً لأنه قد يتحرك بعد الاصطدام

    # --- قسم الرسم ---
    # تعبئة الخلفية
    screen.fill(bg_color)
    
    # رسم كل العناصر
    player1.draw(screen)
    player2.draw(screen)
    ard.draw(screen)
    
    # تحديث العرض
    pygame.display.flip()
    
    # تأخير بسيط لتنظيم سرعة اللعبة
    pygame.time.Clock().tick(60) # تحديد 60 إطار في الثانية