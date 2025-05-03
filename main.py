import pygame

class Main:
    
    def __init__(self):
        
        self.window = pygame.display.set_mode((360, 640))
        self.title = pygame.display.set_caption("Flappy Bird")
        
        self.loop = True
        self.fps = pygame.time.Clock()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.loop = False
    
    def draw(self):
        pass
    
    def updates(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.update()
        
Main().updates()