import pygame

pygame.init()
width, height, fps = 640, 480, 60
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Initial settings
radius = 10
color = (0, 0, 255)
mode = 'draw'  # Available modes: draw, rect, circle, eraser, square, right_triangle, equilateral_triangle, rhombus
drawing = False
last_pos = None
screen_buffer = pygame.Surface((width, height))
screen_buffer.fill((0, 0, 0))

running = True
while running:
    pressed_keys = pygame.key.get_pressed()
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Change color
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            if event.key == pygame.K_g:
                color = (0, 255, 0)
            if event.key == pygame.K_b:
                color = (0, 0, 255)
            # Change mode
            if event.key == pygame.K_e:
                mode = 'eraser'
            if event.key == pygame.K_p:
                mode = 'draw'
            if event.key == pygame.K_o:
                mode = 'circle'
            if event.key == pygame.K_t:
                mode = 'rect'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_y:
                mode = 'right_triangle'
            if event.key == pygame.K_u:
                mode = 'equilateral_triangle'
            if event.key == pygame.K_h:
                mode = 'rhombus'
            # Clear screen
            if event.key == pygame.K_c:
                screen_buffer.fill((0, 0, 0))
            # Adjust brush size
            if event.key == pygame.K_UP:
                radius = min(50, radius + 2)
            if event.key == pygame.K_DOWN:
                radius = max(2, radius - 2)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            if mode in ['circle', 'rect', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                start_pos = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            x1, y1 = start_pos
            x2, y2 = event.pos
            
            if mode == 'circle':
                pygame.draw.circle(screen_buffer, color, start_pos, max(abs(x2 - x1), abs(y2 - y1)))
            
            if mode == 'rect':
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen_buffer, color, rect)
            
            if mode == 'square':
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen_buffer, color, (x1, y1, side, side))
            
            if mode == 'right_triangle':
                pygame.draw.polygon(screen_buffer, color, [(x1, y1), (x1, y2), (x2, y2)])
            
            if mode == 'equilateral_triangle':
                height_triangle = abs(y2 - y1)
                pygame.draw.polygon(screen_buffer, color, [(x1, y2), (x2, y2), ((x1 + x2) // 2, y1)])
            
            if mode == 'rhombus':
                dx, dy = abs(x2 - x1) // 2, abs(y2 - y1) // 2
                pygame.draw.polygon(screen_buffer, color, [(x1 + dx, y1), (x2, y1 + dy), (x1 + dx, y2), (x1, y1 + dy)])
        
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 'draw':
                pygame.draw.line(screen_buffer, color, last_pos, event.pos, radius)
            if mode == 'eraser':
                pygame.draw.circle(screen_buffer, (0, 0, 0), event.pos, radius)
            last_pos = event.pos
    
    # Render everything
    screen.blit(screen_buffer, (0, 0))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()