from obj import *
import pygame
import random

class Game:
    
    def __init__(self):
        
        self.all_sprites = pygame.sprite.Group()
        
        self.speed = 3
        
        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 476, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 476, self.all_sprites)
        
        self.bird = Bird("assets/bird0.png", 50, 320, self.all_sprites)
        
        self.ticks = 0
    
    def draw(self, window):
        self.all_sprites.draw(window)
    
    def update(self):
        self.all_sprites.update()
        self.move_bg()
        self.move_ground()
        self.spawn_pipes()
        
    def move_bg(self):
        self.bg.rect[0] -= 1
        self.bg2.rect[0] -= 1
        
        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 360
        if self.bg2.rect[0] <= -360:
            self.bg2.rect[0] = 360
        
    def move_ground(self):
        self.ground.rect[0] -= self.speed
        self.ground2.rect[0] -= self.speed
        
        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 360
        if self.ground2.rect[0] <= -360:
            self.ground2.rect[0] = 360
    
    def spawn_pipes(self):
        self.ticks += 1
        if self.ticks >= random.randrange(90, 150):
            self.ticks = 0
            pos = random.randrange(285, 420)
            pipe = Pipe("assets/pipe1.png", 360, random.randrange(285, 420), self.all_sprites, speed = self.speed)
            pipe2 = Pipe("assets/pipe2.png", 360, pipe.rect[1] - 490, self.all_sprites, speed = self.speed)
            
            coin = Coin("assets/coin0.png", pipe.rect[0] + 26, pipe.rect[1] - 87, self.all_sprites, speed = self.speed)