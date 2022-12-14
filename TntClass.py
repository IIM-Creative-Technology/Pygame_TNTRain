import pygame 
import random

class Tnt :
        def __init__(self):
                self.x = 100
                self.y = 0
                self.vit = 0.1
                self.width = 30
                self.height = 30
                self.image = pygame.transform.scale(pygame.image.load("object.png"), (30, 30))
        def Move(self):
            self.y += 1*self.vit
            if self.y > 420:
                self.x = random.randrange(640-30)
                self.y = random.randrange(-100, 0)
            return False
        def Draw(self, window):
            window.blit(self.image, (self.x, self.y))