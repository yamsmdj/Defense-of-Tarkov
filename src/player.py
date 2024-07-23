import pygame
from projectile import Projectile

#Classe du Joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 4
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('../assets/scav.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 650
    
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed