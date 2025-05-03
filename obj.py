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


class Coin(Obj):
        
        def __init__(self, img, x, y, *groups, speed = 3):
            super().__init__(img, x, y, *groups, speed = speed)
            
            self.ticks = 0
            
        def update(self, *args):
            self.move()
            self.anim()
        
        def move(self):
            self.rect[0] -= self.speed
            
            if self.rect[0] <= -100:
                self.kill()
        
        def anim(self):
            self.ticks = (self.ticks + 1) % 6
            self.image = pygame.image.load(f"assets/coin{self.ticks}.png")
            

class Bird(Obj):
    
    def __init__(self, img, x, y, *groups, speed = 1):
        super().__init__(img, x, y, *groups, speed = speed)
        
        self.ticks = 0
        self.gravity = 0.5
        
        self.alive = True
        
    def update(self, *args):
        self.anim()
        self.move()
    
    def anim(self):
        self.ticks = (self.ticks + 1) % 4
        self.image = pygame.image.load(f"assets/bird{self.ticks}.png")
    
    def move(self):
        key = pygame.key.get_pressed()
        
        self.speed += self.gravity
        self.rect[1] += self.speed
        
        if self.speed >= 10:
            self.speed = 10
        
        if key[pygame.K_SPACE]:
            self.speed -= 2
        
        if self.rect[1] >= 430:
            self.rect[1] = 429
            self.speed = 0
        elif self.rect[1] <= 0:
            self.rect[1] = 0
            self.speed = 4
    
    def colision_pipe(self, group):
        
        col = pygame.sprite.spritecollide(self, group, False)
        
        if col:
            self.alive = False
    
    def colision_coin(self, group):
        
        col = pygame.sprite.spritecollide(self, group, True)
        
        if col:
            print("Moeda")
