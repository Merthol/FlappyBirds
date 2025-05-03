import pygame


class Obj(pygame.sprite.Sprite):
    
    def __init__(self, img, x, y, *groups, speed = 1):
        super().__init__(*groups)
        
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.speed = speed


class Pipe(Obj):
    
    def __init__(self, img, x, y, *groups, speed = 3):
        super().__init__(img, x, y, *groups, speed = speed)
        
    def update(self):
        self.move()
    
    def move(self):
        self.rect[0] -= self.speed
        
        if self.rect[0] <= -100:
            self.kill()
