import pygame
import random
import sys

pygame.init()
pygame.mixer.init()  # Инициализация микшера для воспроизведения звука

# Загружаем и воспроизводим музыку
pygame.mixer.music.load('C:/Users/Admin/Documents/Demo/Lab8/my_music')
pygame.mixer.music.play(-1)  # -1 означает зацикленное воспроизведение

# Устанавливаем размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()  # Создаем таймер для управления FPS


font = pygame.font.Font(None, 30)

# Определяем цвета в формате (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Цвет змейки
RED = (255, 1, 0)    # Цвет еды
BLACK = (0, 0, 0)    # Цвет фона

# Начальная позиция змейки
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]   # Тело змейки состоит из нескольких сегментов
snake_direction = "RIGHT"  # Начальное направление движения
change_to = snake_direction
speed = 10

# Позиция еды (случайная)
def spawn_food():
    while True:
        pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        if pos not in snake_body:
            return pos

food_pos = spawn_food()
food_spawn = True  # Флаг, показывающий, появилась ли еда

game_score = 0    # Начальный счет
level = 1

isRunning = True  # Флаг работы игры

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Если нажата кнопка "Закрыть"
            isRunning = False
            sys.exit()      # Закрываем программу
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"    

    # Меняем направление движения змейки
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Добавляем новую голову змейки
    snake_body.insert(0, list(snake_pos))  
   
    # Проверяем, съела ли змейка еду
    if snake_pos == food_pos:
        food_spawn = False
        game_score += 1    # Увеличиваем счет
        if game_score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()   # Убираем хвост, если не съела еду
    
    # Если еда была съедена, создаем новую в случайном месте
    if not food_spawn:
        food_pos = spawn_food()
    food_spawn = True

    # Проверяем, врезалась ли змейка в стену
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False

    # Проверяем, врезалась ли змейка сама в себя
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False   # Завершаем игру
    # Очищаем экран
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    # Отрисовываем еду
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Отображаем счет
    score_text = font.render(f"Score: {game_score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))
    
    pygame.display.update()
    clock.tick(speed)  # Устанавливаем скорость игры
# Отображаем сообщение "GAME OVER"   
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)
