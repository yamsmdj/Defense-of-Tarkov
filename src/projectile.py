import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.speed = 1.2
        self.player = player
        self.image = pygame.image.load('../assets/balle.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 70

    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x += self.speed

        #condition verifier si projectile n'est plus present sur l'ecran
        if self.rect.x > 1280: 
            #supprimer le projectile
            self.remove()

