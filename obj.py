import pygame


class Obj(pygame.sprite.Sprite):
    
    def __init__(self, img, x, y, *groups, speed = 1):
        super().__init__(*groups)
        
        pygame.mixer.init()
        
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
        
        self.sound_point = pygame.mixer.Sound("assets/sounds/point.ogg")  # Carrega o som de pontos
        self.sound_hit = pygame.mixer.Sound("assets/sounds/hit.ogg")  # Carrega o som de bloqueio
        self.sound_wing = pygame.mixer.Sound("assets/sounds/wing.ogg")  # Carrega o som de pontos
        
        self.ticks = 0
        self.gravity = 0.5
        
        self.score = 0
        
        self.alive = True
        
        self.space_pressed = False
        
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
            if self.space_pressed == False:
                self.space_pressed = True
                self.sound_wing.play()
            self.speed -= 2
        else:
            self.space_pressed = False
        
        if self.rect[1] >= 430:
            self.rect[1] = 429
            self.speed = 0
        elif self.rect[1] <= 0:
            self.rect[1] = 0
            self.speed = 4
    
    def colision_pipe(self, group):
        
        col = pygame.sprite.spritecollide(self, group, False)
        
        if col:
            self.sound_hit.play()
            self.alive = False
    
    def colision_coin(self, group):
        
        col = pygame.sprite.spritecollide(self, group, True)
        
        if col:
            self.sound_point.play()
            self.score += 1


class Text:
    
    def __init__(self, size, text):
        
        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text, True, (255, 255, 255))
        
    def draw(self, window, x, y):
        window.blit(self.render, (x, y))
    
    def text_update(self, text):
        self.render = self.font.render(text, True, (255, 255, 255))
