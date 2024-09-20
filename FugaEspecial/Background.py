import pygame

class Background:
    image = None  # Atributo para a imagem

    def __init__(self):
        # Carrega a imagem do fundo
        Background_fig = pygame.image.load("Images/background.png")
        Background_fig = Background_fig.convert()  # Otimiza o formato da imagem
        self.image = Background_fig  # Atribui a imagem ao atributo da classe

    def update(self, dt):
        pass  # Aqui você pode adicionar lógica para atualizar o plano de fundo, se necessário

    def draw(self, screen):
        screen.blit(self.image, (0, 0))  # Desenha a imagem do fundo na tela
