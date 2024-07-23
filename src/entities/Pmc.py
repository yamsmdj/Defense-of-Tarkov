import pygame

class Pmc(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('pmc.png')  # Charge une image de pmc
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 100