import pygame
from game import Game
pygame.init()


#Generer la fenetre du jeu
screen = pygame.display.set_mode((1280, 960))
#Titre fenetre
pygame.display.set_caption("Defense of Tarkov")
#background (etape 1)
background = pygame.image.load('../assets/bg.jpg')

#Charger le joueur de la classe Player
#player = Player()
#Charger le jeux 
game = Game()


running = True
#Boucle du jeu
while running:

    #appliquer le background
    screen.blit(background, (0, 0))

    #appliquer l'image du joueur 
    screen.blit(game.player.image, game.player.rect)

    #recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    #appliquer image du projectile
    game.player.all_projectiles.draw(screen)

    # Joueur -> gauche/droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() :
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Mettre a jour l'affichage
    pygame.display.flip()


    for event in pygame.event.get():
        #fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        #Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
      

