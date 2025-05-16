import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooter Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 20
player_speed = 5

# Bullet (fireball) settings
bullets = []
bullet_speed = 10
bullet_size = 10

# Game loop variables
clock = pygame.time.Clock()
running = True

def draw_player(pos):
    pygame.draw.rect(screen, BLUE, (pos[0] - player_size // 2, pos[1] - player_size // 2, player_size, player_size))

def draw_bullet(pos):
    pygame.draw.circle(screen, RED, (int(pos[0]), int(pos[1])), bullet_size // 2)

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Shoot a bullet towards the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - player_pos[0]
            dy = mouse_y - player_pos[1]
            distance = math.sqrt(dx**2 + dy**2)
            if distance != 0:  # Avoid division by zero
                bullet_vel = [dx / distance * bullet_speed, dy / distance * bullet_speed]
                bullets.append([player_pos[0], player_pos[1], bullet_vel[0], bullet_vel[1]])

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos[1] > player_size:
        player_pos[1] -= player_speed
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed
    if keys[pygame.K_a] and player_pos[0] > player_size:
        player_pos[0] -= player_speed
    if keys[pygame.K_d] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Update bullets
    for bullet in bullets[:]:
        bullet[0] += bullet[2]  # Update x position
        bullet[1] += bullet[3]  # Update y position
        if bullet[0] < 0 or bullet[0] > WIDTH or bullet[1] < 0 or bullet[1] > HEIGHT:
            bullets.remove(bullet)

    # Draw everything
    screen.fill(WHITE)  # Background
    draw_player(player_pos)
    for bullet in bullets:
        draw_bullet(bullet)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Quit Pygame
pygame.quit()