from obj import Obj
import pygame

class Game:
    
    def __init__(self):
        
        self.all_sprites = pygame.sprite.Group()
        
        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 476, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 476, self.all_sprites)
    
    def draw(self, window):
        self.all_sprites.draw(window)
    
    def update(self):
        self.all_sprites.update()
        self.move_bg()
        self.move_ground()
        
    def move_bg(self):
        self.bg.rect[0] -= 1
        self.bg2.rect[0] -= 1
        
        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 360
        if self.bg2.rect[0] <= -360:
            self.bg2.rect[0] = 360
        
    def move_ground(self):
        self.ground.rect[0] -= 2
        self.ground2.rect[0] -= 2
        
        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 360
        if self.ground2.rect[0] <= -360:
            self.ground2.rect[0] = 360