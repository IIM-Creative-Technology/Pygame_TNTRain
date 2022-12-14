import pygame
from PlayerClass import Player
from TntClass import Tnt
from HealClass import Heal
from CoinClass import Coin

p = Player()
pygame.init()
pygame.display.set_caption("Minecraft TNT Rain 'Impossible Edition'")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
width = 640
height = 480
game_window = pygame.display.set_mode((width, height))

Tnts = [Tnt(), Tnt()]
Heals = [Heal()]
Coins = [Coin()]

background = pygame.image.load("background.jpg")
font = pygame.font.SysFont("comicsans", 30, True)
score = 0
font2 = pygame.font.SysFont("comicsans", 30, True)
health = 5

while True:
    
    game_window.blit(pygame.transform.scale(
        background, (width, height)), (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        p.Move(-p.vit, 0)
        
    if keys[pygame.K_RIGHT]:
        p.Move(p.vit, 0)
        
    for t in Tnts:
        t.Move()
        t.Draw(game_window)
        
    for h in Heals:
        h.Move()
        h.Draw(game_window)
        
    for c in Coins:
        c.Move()
        c.Draw(game_window)
        
    if p.x < 0:
        p.x = 0
        
    if p.x > width - p.width:
        p.x = width - p.width
        
    for t in Tnts:
        if t.y + t.height > p.y:
            if t.x + t.width > p.x and t.x < p.x + p.width:
                Tnts.append(Tnt())
                Tnts.remove(t)
                p.health -= 1
                health -= 1
                
                if p.health <= 0:
                    text = font.render("Game Over", 1, WHITE)
                    game_window.blit(
                        text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    p = Player()
                    Tnts = [Tnt(), Tnt()]
                    Heals = [Heal()]
                    score = 0
                    health = 5
                    
    for h in Heals:
        if h.y + h.height > p.y:
            if h.x + h.width > p.x and h.x < p.x + p.width:
                Heals.append(Heal())
                Heals.remove(h)
                p.health += 1
                health += 1
                
    for c in Coins:
        if c.y + c.height > p.y:
            if c.x + c.width > p.x and c.x < p.x + p.width:
                Coins.append(Coin())
                Coins.remove(c)
                score += 1
                
    text = font.render("Score: " + str(score), 1, WHITE)
    game_window.blit(text, (10, 10))
    text2 = font2.render("Health: " + str(health), 1, WHITE)
    game_window.blit(text2, (width - text2.get_width() - 10, 10))
    p.Draw(game_window)
    pygame.display.flip()