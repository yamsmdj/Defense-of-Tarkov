import pygame

class Scav(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Scav.png')  # Charge une image de Scav
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 100
        self.speed = 1