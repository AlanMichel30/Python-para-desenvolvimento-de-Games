import pygame

class Player:
    """
    Esta classe define Jogador
    """
    image = None
    x = None
    y = None

    def __init__(self, x, y):
        player_fig = pygame.image.load("Images/player.png")
        player_fig = player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (90, 90))
        self.image = player_fig
        self.x = x
        self.y = y

    # Criar o Player
    def draw (self, screen, x, y):
        screen.blit(self.image, (x, y))    


