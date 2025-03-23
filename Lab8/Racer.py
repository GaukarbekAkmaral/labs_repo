import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
ROAD_WIDTH = 300
LANE_WIDTH = ROAD_WIDTH // 3
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Настройки экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Загрузка изображений
car_image = pygame.image.load("car1.png")
car_image = pygame.transform.scale(car_image, (50, 100))
coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))

# Класс автомобиля
class Car:
    def __init__(self):
        self.image = car_image
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT - 50))
        self.speed = 5
    
    def move(self, direction):
        if direction == "left" and self.rect.left > (WIDTH - ROAD_WIDTH) // 2:
            self.rect.x -= LANE_WIDTH
        if direction == "right" and self.rect.right < (WIDTH + ROAD_WIDTH) // 2:
            self.rect.x += LANE_WIDTH
    
    def draw(self):
        screen.blit(self.image, self.rect)

# Класс монет
class Coin:
    def __init__(self):
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([(WIDTH - ROAD_WIDTH) // 2 + LANE_WIDTH * i + 15 for i in range(3)])
        self.rect.y = -50
        self.speed = 5
    
    def update(self):
        self.rect.y += self.speed
    
    def draw(self):
        screen.blit(self.image, self.rect)

# Инициализация игры
car = Car()
coins = []
coin_spawn_time = 0
coins_collected = 0
font = pygame.font.Font(None, 36)

# Игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(GRAY)
    
    # Рисуем дорогу
    pygame.draw.rect(screen, BLACK, [(WIDTH - ROAD_WIDTH) // 2, 0, ROAD_WIDTH, HEIGHT])
    
    # Рисуем разделительные линии
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, YELLOW, (WIDTH//2 - 5, i, 10, 20))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.move("left")
            if event.key == pygame.K_RIGHT:
                car.move("right")
    
    # Добавление новых монет
    if pygame.time.get_ticks() - coin_spawn_time > 1000:
        coins.append(Coin())
        coin_spawn_time = pygame.time.get_ticks()
    
    # Обновление и отрисовка монет
    for coin in coins[:]:
        coin.update()
        if coin.rect.top > HEIGHT:
            coins.remove(coin)
        if car.rect.colliderect(coin.rect):
            coins_collected += 1
            coins.remove(coin)
        coin.draw()
    
    # Отрисовка автомобиля
    car.draw()
    
    # Отображение счетчика монет
    score_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 20))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
