import pygame
import random
import sys

pygame.init()
pygame.mixer.init()  # Инициализация микшера для воспроизведения звука

# Загружаем и воспроизводим музыку
pygame.mixer.music.load('C:/Users/Admin/Documents/Demo/Lab8/my_music.mp3')
pygame.mixer.music.play(-1)  # -1 означает зацикленное воспроизведение

# Размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)

# Определяем цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Цвет змейки
RED = (255, 0, 0)  # Обычная еда
BLUE = (0, 0, 255)  # Особая еда (даёт больше очков)
BLACK = (0, 0, 0)  # Цвет фона

# Настройки змейки
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]  # Начальная длина змейки
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10

game_score = 0
level = 1
isRunning = True

# Настройки еды (исчезает через некоторое время)
food_types = {"normal": (RED, 1), "special": (BLUE, 3)}  # Цвета и очки за еду
food_spawn_time = 0  # Время появления еды
food_lifetime = 1500  # Через сколько кадров еда исчезает

def spawn_food():
    """Генерирует еду в случайном месте с разным весом."""
    while True:
        pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        if pos not in snake_body:
            food_type = random.choice(list(food_types.keys()))  # Выбираем тип еды (обычная/особая)
            return pos, food_types[food_type][0], food_types[food_type][1]  # Позиция, цвет, очки

food_pos, food_color, food_value = spawn_food()
food_spawn = True
food_spawn_time = pygame.time.get_ticks()

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Управление змейкой
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
    
    # Меняем направление движения
    snake_direction = change_to
    moves = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}
    snake_pos[0] += moves[snake_direction][0]
    snake_pos[1] += moves[snake_direction][1]
    
    # Добавляем новую голову змейки
    snake_body.insert(0, list(snake_pos))
    
    # Проверяем, съела ли змейка еду
    if snake_pos == food_pos:
        food_spawn = False
        game_score += food_value  # Увеличиваем счёт в зависимости от типа еды
        if game_score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()  # Убираем хвост, если не съела еду
    
    # Проверяем, не истекло ли время жизни еды
    if pygame.time.get_ticks() - food_spawn_time > food_lifetime:
        food_spawn = False  # Убираем еду, если прошло слишком много времени
    
    # Создаём новую еду, если старая исчезла
    if not food_spawn:
        food_pos, food_color, food_value = spawn_food()
        food_spawn = True
        food_spawn_time = pygame.time.get_ticks()  # Сбрасываем таймер еды
    
    # Проверяем столкновение со стенами
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False
    
    # Проверяем, не столкнулась ли змейка сама с собой
    if snake_pos in snake_body[1:]:
        isRunning = False
    
    # Очищаем экран и отрисовываем всё заново
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Отображаем счёт и уровень
    score_text = font.render(f"Счёт: {game_score}  Уровень: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))
    
    pygame.display.update()
    clock.tick(speed)

# Отображаем сообщение "Игра окончена"
screen.fill(BLACK)
game_over_text = font.render("ИГРА ОКОНЧЕНА", True, WHITE)
game_over_rectangle = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)
