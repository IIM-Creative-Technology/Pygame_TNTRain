import pygame

class Player :
        def __init__(self):
                self.x = 270
                self.y = 400
                self.vit = 0.25
                self.width = 34
                self.height = 68
                self.health = 5
                self.image = pygame.transform.scale(pygame.image.load("player.png"), (self.width, self.height))
                self.image_left = pygame.transform.scale(pygame.image.load("player_left.png"), (self.width, self.height))
                self.image_right = pygame.transform.scale(pygame.image.load("player_right.png"), (self.width, self.height))
        def Move(self, x, y):
                self.x += x
                self.y += y
        def Draw(self, window):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player = self.image_left
            elif keys[pygame.K_RIGHT]:
                player = self.image_right
            else:
                player = self.image
            window.blit(player, (self.x, self.y))