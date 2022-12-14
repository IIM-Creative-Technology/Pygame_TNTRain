# Importation des modules.
# Importation de la bibliothèque Pygame, qui permet de créer des jeux vidéo en Python.
import pygame
# Importation de la bibliothèque random, qui permet de générer des nombres aléatoires.
import random

# Initialisation de la bibliothèque Pygame.
pygame.init()

# Nom du jeu.
pygame.display.set_caption("Minecraft TNT Rain 'Impossible Edition'")

# Définition des couleurs, en utilisant le format RGB (Red, Green, Blue).
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Création de la fenêtre de jeu, avec une taille de 640 pixels de large et 480 pixels de haut.
width = 640
height = 480

# Création de la fenêtre de jeu avec la fonction set_mode() de la bibliothèque Pygame.
game_window = pygame.display.set_mode((width, height))

# Définition des variables de jeu, dimensions du personnage, position du personnage, vitesse du personnage, nombre de vies du personnage, score du personnage.
player_x = width / 2 - 20 / 2
player_y = height - 140
player_speed = 10
player_width = 50
player_height = 100
player_life = 5
player_score = 0
player_animation = 2

# Définition des variables de jeu, dimensions des objets qui tombent du ciel, position des objets qui tombent du ciel, vitesse des objets qui tombent du ciel.
object_x = random.randint(0, width - 20)
object_y = 0
object_speed = 10
object_width = 40
object_height = 40

# Définition des variables de jeu, dimensions des objets qui tombent du ciel, position des objets qui tombent du ciel, vitesse des objets qui tombent du ciel.
object2_x = object_x
object2_y = object_y
object2_speed = object_speed
object2_width = object_width
object2_height = object_height

# Définition des variables de jeu, dimensions de la vie qui tombent du ciel, position de la vie qui tombent du ciel, vitesse de la vie qui tombent du ciel.
life_x = random.randint(0, width - 20)
life_y = 0
life_speed = 15
life_width = 40
life_height = 40

# Boucle principale du jeu, qui permet de faire tourner le jeu en permanence et de gérer les événements qui se produisent pendant le jeu.
while True:
    
    # Vérifie si l'utilisateur a cliqué sur la croix rouge de la fenêtre de jeu, pour fermer le jeu et arrêter la boucle principale tout en nettoyant les ressources utilisées par Pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Affichage des objets qui tombent du ciel.
    game_window.blit(pygame.transform.scale(pygame.image.load("object.png"), (object_width, object_height)), (object_x, object_y))
    game_window.blit(pygame.transform.scale(pygame.image.load("object.png"), (object2_width, object2_height)), (object2_x, object2_y))
    # Affichage des coeurs qui tombent du ciel.
    game_window.blit(pygame.transform.scale(pygame.image.load("heart.png"), (life_width, life_height)), (life_x, life_y))

    # Vérifie si l'utilisateur a appuyé sur une touche du clavier, pour déplacer le personnage.
    keys = pygame.key.get_pressed()
    # Si la touche flèche gauche est appuyée, le personnage se déplace vers la gauche.
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        # Si la touche flèche gauche est appuyée, le personnage change d'apparence.
        player_animation = 1
    # Si la touche flèche droite est appuyée, le personnage se déplace vers la droite.
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        # Si la touche flèche droite est appuyée, le personnage change d'apparence.
        player_animation = 0
    object_y += object_speed
    object2_y += object2_speed
    life_y += life_speed
    
    # Quand auncune touche n'est appuyée, le personnage reste immobile.
    if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
        # Apparance par défaut du personnage (immobile).
        player_animation = 2
    
    # Permet de définir les limites de déplacement du personnage et des objets, pour qu'il ne sorte pas de la fenêtre de jeu.
    if player_x <= 0:
        player_x = 0
    if player_x >= width - player_width:
        player_x = width - player_width
    if object_y >= height:
        object_y = 0
        object_x = random.randint(0, width - 20)
    if object2_y >= height:
        object2_y = 0
        object2_x = random.randint(0, width - 20)
    if life_y >= height:
        life_y = 0
        life_x = random.randint(0, width - 20)

    # Si l'objet "object" touche le personnage, le personnage perd une vie
    if object_x + object_width >= player_x and object_x <= player_x + player_width and object_y + object_height >= player_y and object_y <= player_y + player_height:
        player_life -= 1
        object_y = 0
        object_x = random.randint(0, width - 20)   
    
    # Si l'objet "object" touche le personnage, le personnage perd une vie
    if object2_x + object2_width >= player_x and object2_x <= player_x + player_width and object2_y + object2_height >= player_y and object2_y <= player_y + player_height:
        player_life -= 1
        object2_y = 0
        object2_x = random.randint(0, width - 20)    

    # Si l'objet "life" touche le personnage, le personnage gagne une vie
    if life_x + life_width >= player_x and life_x <= player_x + player_width and life_y + life_height >= player_y and life_y <= player_y + player_height:
        player_life += 1
        life_y = 0
        life_x = random.randint(0, width - 20)

    # Vérifie si le personnage n'a plus de vie, pour afficher un message de fin de jeu et remettre le score et le nombre de vies du personnage à 0.
    if player_life == 0:
        # Affiche un message de fin de jeu.
        game_window.blit(pygame.font.SysFont("Arial", 20).render("Game Over", True, WHITE), (width / 2 - 50, height / 2 - 10))
        # Affiche le score du personnage.
        game_window.blit(pygame.font.SysFont("Arial", 20).render("Score: " + str(player_score), True, WHITE), (width / 2 - 50, height / 2 + 10))
        # Met à jour l'affichage de la fenêtre de jeu.
        pygame.display.update()
        # Attend 5 secondes avant de remettre le score et le nombre de vies du personnage à 0.
        pygame.time.wait(5000)
        # Remet le nombre de vies du personnage à 5.
        player_life = 5
        # Remet le score du personnage à 0.
        player_score = 0
        # Fait réapparaître l'objet à un endroit aléatoire de la fenêtre de jeu.
        object_y = 0
        object_x = random.randint(0, width - 20)
        object2_y = 0
        object2_x = random.randint(0, width - 20)
        # Fait réapparaître les points de vie à un endroit aléatoire de la fenêtre de jeu.
        life_y = 0
        life_x = random.randint(0, width - 20)

    # Vérifie si l'objet qui tombe du ciel est arrivé au sol, pour augmenter la vitesse de l'objet, augmenter la taille de l'objet, augmenter le score du personnage et diminuer la vitesse du personnage.
    if object_y == 0:
        # Augmente la vitesse de l'objet qui tombe du ciel.
        object_speed += 0.25
        # Augmente la taille de l'objet qui tombe du ciel.
        object_height += 0.1
        object_width += 0.1
        # Augmente la vitesse du coeur qui tombe du ciel jusqu'à 30.
        if life_speed > 1:
            life_speed -= 1
        # Réduit la taille du coeur qui tombe du ciel.
        life_height -= 0.1
        life_width -= 0.1
        # Augmente le score du personnage.
        player_score += 1
        # Diminue la vitesse du personnage.
        player_speed -= 0.1
    
    # Si le joueur appuie sur la touche Echap, le jeu se ferme.
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    if player_animation == 0:
        # Affichage du personnage qui se déplace vers la droite.
        game_window.blit(pygame.transform.scale(pygame.image.load("player_right.png"), (player_width, player_height)), (player_x, player_y))
    elif player_animation == 1:
        # Affichage du personnage qui se déplace vers la gauche.
        game_window.blit(pygame.transform.scale(pygame.image.load("player_left.png"), (player_width, player_height)), (player_x, player_y))
    else:
        # Affichage du personnage immobile.
        game_window.blit(pygame.transform.scale(pygame.image.load("player.png"), (player_width, player_height)), (player_x, player_y))
    
    # Affichage du score du personnage.
    game_window.blit(pygame.font.SysFont("Arial", 20).render("Score: " + str(player_score), True, WHITE), (15, 10))
    # Affichage du nombre de vies du personnage.
    game_window.blit(pygame.font.SysFont("Arial", 20).render("Life: " + str(player_life), True, WHITE), (width - 70, 10))

    # Actualisation de la fenêtre de jeu.
    pygame.display.update()
    # Affichage de l'image de fond.
    game_window.blit(pygame.transform.scale(pygame.image.load("background.jpg"), (width, height)), (0, 0))
    # Définition de la vitesse de rafraîchissement de la fenêtre de jeu, pour éviter que le jeu ne tourne trop vite.
    pygame.time.Clock().tick(60)