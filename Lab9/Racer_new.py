import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Настройки игры
FPS = 60
FramePerSec = pygame.time.Clock()
SPEED = 7  # Начальная скорость врага
SCORE = 0
COINS = 0
COIN_SPEED = 4  # Скорость падения монет
COIN_THRESHOLD = 5  # Количество монет для увеличения скорости врага

# Загрузка изображений
background = pygame.image.load("AnimatedStreet1.png")
player_img = pygame.image.load("car2.png")
enemy_img = pygame.image.load("car1.png")
coin_img = pygame.image.load("coin.png")

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

P1 = Player()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if not self.rect.colliderect(P1.rect):  # Убедимся, что враг не спавнится на игроке
                break

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

E1 = Enemy()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Спавн вверху экрана
        self.speed = COIN_SPEED  # Скорость падения монет
        self.value = random.randint(1, 3)  # Вес монеты (очки)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:  # Если монета вышла за экран, удалить
            self.kill()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)

# Таймеры
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Увеличение скорости врагов
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 2000)  # Спавн монет каждые 2 секунды

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == SPAWN_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Обновление фона
    DISPLAYSURF.blit(background, (0, 0))
    
    # Отображение счета
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Движение спрайтов
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    coins.update()  # Обновляем монеты, чтобы они падали
    
    # Проверка на столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка на сбор монеты
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        COINS += coin.value  # Добавляем вес монеты к общему счету
        
    # Увеличение скорости врага, если собрано N монет
    if COINS >= COIN_THRESHOLD:
        SPEED += 1
        COIN_THRESHOLD += 5  # Следующий порог увеличения скорости
    
    # Увеличиваем скорость врагов каждые 5 собранных монет
    #if COINS % 5 == 0 and COINS > 0:
    #    SPEED += 0.5
    
    pygame.display.update()
    FramePerSec.tick(FPS)
