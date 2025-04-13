import pygame
import random
import sys

# Импортируем функции для работы с базой данных
from user_db import get_or_create_user, save_user_progress

pygame.init()
pygame.mixer.init() 

# Загружаем и воспроизводим музыку
pygame.mixer.music.load('C:/Users/Admin/Documents/Demo/Lab8/my_music.mp3')
pygame.mixer.music.play(-1)  

# Размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)

# Определяем цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  
RED = (255, 0, 0)  
BLUE = (0, 0, 255)  
BLACK = (0, 0, 0)  

# Запрос имени пользователя
username = input("Введите имя пользователя: ")
user_id, game_score, level = get_or_create_user(username)  

# Настройки игры
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]  
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10

isRunning = True
game_paused = False

# Настройки еды
food_types = {"normal": (RED, 1), "special": (BLUE, 3)}
food_pos, food_color, food_value = spawn_food()

# Главное игровое состояние
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
            if event.key == pygame.K_p:  
                game_paused = not game_paused  # Переключение паузы

    if game_paused:
        # Отображаем "Пауза" на экране
        pause_text = font.render("Пауза. Нажмите P для продолжения.", True, WHITE)
        screen.blit(pause_text, (WIDTH / 4, HEIGHT / 2))
        pygame.display.update()
        clock.tick(10)  # Замедляем игру во время паузы
        continue

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
        game_score += food_value  # Увеличиваем счёт
        if game_score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()  # Убираем хвост, если не съела еду
    
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

    # Сохраняем текущий счёт и уровень в базу данных
    if not game_paused:
        save_user_progress(user_id, game_score, level)  # Сохранение прогресса
