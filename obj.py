import pygame


class Obj(pygame.sprite.Sprite):
    
    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
