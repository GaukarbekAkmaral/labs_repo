import pygame

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        pass
    
    def Update(self):
        pass
    
    def Render(self, screen):
        pass
    
    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

class PaintScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.radius = 10
        self.color = (0, 0, 255)
        self.mode = 'draw'  # draw, rect, circle, eraser
        self.last_pos = None
        self.drawing = False
        self.screen_buffer = pygame.Surface((640, 480))
        self.screen_buffer.fill((0, 0, 0))
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    self.color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    self.color = (0, 0, 255)
                elif event.key == pygame.K_e:
                    self.mode = 'eraser'
                elif event.key == pygame.K_p:
                    self.mode = 'draw'
                elif event.key == pygame.K_o:
                    self.mode = 'circle'
                elif event.key == pygame.K_t:
                    self.mode = 'rect'
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.drawing = True
                self.last_pos = event.pos
                if self.mode in ['circle', 'rect']:
                    self.start_pos = event.pos
                
            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawing = False
                if self.mode == 'circle':
                    pygame.draw.circle(self.screen_buffer, self.color, self.start_pos, max(abs(event.pos[0] - self.start_pos[0]), abs(event.pos[1] - self.start_pos[1])))
                elif self.mode == 'rect':
                    pygame.draw.rect(self.screen_buffer, self.color, (*self.start_pos, event.pos[0] - self.start_pos[0], event.pos[1] - self.start_pos[1]))
                
            elif event.type == pygame.MOUSEMOTION and self.drawing:
                if self.mode == 'draw':
                    pygame.draw.line(self.screen_buffer, self.color, self.last_pos, event.pos, self.radius)
                elif self.mode == 'eraser':
                    pygame.draw.circle(self.screen_buffer, (0, 0, 0), event.pos, self.radius)
                self.last_pos = event.pos
    
    def Render(self, screen):
        screen.blit(self.screen_buffer, (0, 0))


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    active_scene = starting_scene

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()
        filtered_events = [event for event in pygame.event.get() if event.type != pygame.QUIT]
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Render(screen)
        pygame.display.flip()
        clock.tick(fps)

run_game(640, 480, 60, PaintScene())
