import pygame
import random

# Инициализация pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 400, 600  # Сделали окно уже
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Enemy")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Игрок
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Враг
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 7  # Увеличили скорость врага


# Игровой цикл
running = True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)
    
    # Проверка столкновения
    if (player_x < enemy_x < player_x + player_size or player_x < enemy_x + enemy_size < player_x + player_size) and \
       (player_y < enemy_y < player_y + player_size or player_y < enemy_y + enemy_size < player_y + player_size):
        print("Game Over")
        running = False
    
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(window, RED, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.display.update()

pygame.quit()
