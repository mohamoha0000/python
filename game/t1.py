import pygame
import sys

# تهيئة مكتبة Pygame
pygame.init()

# إعداد نافذة العرض
width, height = 1540, 880
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Rectangle")




bg_color=(0,0,0)

def cond(p,p2):
    return p.x<p2.x+p2.width and p2.x<p.x+p.width and p.y<p2.y+p2.height and p2.y<p.y+p.height
class player:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.n=0
        self.dr=0
        self.color=color
    def draw(self):
        pygame.draw.rect(screen,self.color, (self.x,self.y,self.width,self.height))
        if(self.n>0):
            if(self.x+self.dr*(self.n)>0 and self.x+self.dr*(self.n)<width-self.width):
                self.x+=self.dr*(self.n)
                self.n-=0.5
            else:
                self.dr*=-1
player1=player(0,(height/2)-50,50,50,(255,255,255))
player2=player(width/2,(height/2)-50,50,50,(255,0,0))
ard=player(0,height/2,width,20,(255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                player1.n=20
                player1.dr=1
            if event.key == pygame.K_a:
                player1.n=20
                player1.dr=-1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
        pass#player1.x+=4
    # تعبئة الخلفية
    if(cond(player1,player2)):
        if(player1.dr == player2.dr):
            if(player2.n>player1.n):
                player2.n=player2.n-player1.n
                player1.n+=player2.n-player1.n
            else:
                player2.n+=player1.n-player2.n
                player1.n=player1.n-player2.n
        else:
            if(player2.n>player1.n):
                player1.dr=player2.dr
                player1.n=player2.n
                player2.n=player2.n-player1.n
            else:
                player2.dr=player1.dr
                player2.n=player1.n
                player1.n=player1.n-player2.n
    screen.fill(bg_color)
    player1.draw()
    player2.draw()
    ard.draw()
    # تحديث العرض
    pygame.display.flip()
    pygame.time.delay(10)
