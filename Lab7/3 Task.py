import pygame
import time
import math
import os

# Инициализация Pygame
pygame.init()

WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
BACKGROUND_COLOR = (255, 255, 255)

# 1. Часы с руками Микки Мауса
mickey = pygame.image.load("mickey.png")
mickey = pygame.transform.scale(mickey, (WIDTH, HEIGHT))

minute_hand = pygame.image.load("minute_hand.png")
second_hand = pygame.image.load("second_hand.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def draw_hand(image, angle, length):
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center=(CENTER[0] + length * math.cos(math.radians(angle - 90)),
                                          CENTER[1] + length * math.sin(math.radians(angle - 90))))
    screen.blit(rotated_image, rect.topleft)

# 2. Музыкальный плеер
pygame.mixer.init()
music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0
pygame.mixer.music.load(music_files[current_track])

# 3. Красный шар
ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(mickey, (0, 0))
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minute_angle = (minutes % 60) * 6
    second_angle = (seconds % 60) * 6
    
    draw_hand(minute_hand, minute_angle, 70)
    draw_hand(second_hand, second_angle, 90)
    

    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Управление шаром
            if event.key == pygame.K_UP and ball_y - ball_radius - ball_speed >= 0:
                ball_y -= ball_speed
            elif event.key == pygame.K_DOWN and ball_y + ball_radius + ball_speed <= HEIGHT:
                ball_y += ball_speed
            elif event.key == pygame.K_LEFT and ball_x - ball_radius - ball_speed >= 0:
                ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT and ball_x + ball_radius + ball_speed <= WIDTH:
                ball_x += ball_speed
            # Управление музыкой
            elif event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()

pygame.quit()
