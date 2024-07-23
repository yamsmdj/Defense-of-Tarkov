import pygame
import sys

class Grille:
    def __init__(self, screen, rows, cols, hauteur):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.hauteur = hauteur
        self.width, self.height = self.screen.get_size()
        self.cell_width = self.width // self.cols
        self.cell_height = (self.height - self.hauteur) // self.rows

    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * self.cell_width, self.hauteur + row * self.cell_height, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)


class Game:
     
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Defense of Tarkov")
        self.background = pygame.image.load('assets/images/bg-tarkov.jpg')
        self.running = True 
        self.hauteur = 100
        self.grille = Grille(self.screen, 4, 7, self.hauteur)

    def main_function(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(self.background, (0, 0))
            self.grille.draw()
            self.draw_ui()
            pygame.display.flip()
    
    def draw_ui(self):
        # Dessiner un rectangle en haut de l'écran pour l'interface utilisateur
        ui_rect = pygame.Rect(0, 0, self.screen.get_width(), self.hauteur)
        pygame.draw.rect(self.screen, (0, 0, 0), ui_rect)  # Remplir l'UI avec une couleur noire
        # Ajouter ici le dessin des éléments UI comme les soleils, les plantes, etc.
        font = pygame.font.SysFont(None, 36)
        text = font.render('Roubles: 100', True, (255, 255, 255))
        self.screen.blit(text, (10, 10))


if __name__ == '__main__':
    pygame.init()
    Game().main_function()
    pygame.quit()
    