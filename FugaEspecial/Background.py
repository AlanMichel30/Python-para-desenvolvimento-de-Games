import pygame

class Background:
    image = None  # Atributo para a imagem
    margin_left = None
    margin_right = None

    def __init__(self):
        # Carrega a imagem do fundo e ajusta para o tamanho da tela (800x600)
        Background_fig = pygame.image.load("Images/background.png")
        Background_fig = Background_fig.convert()  # Otimiza o formato da imagem
        Background_fig = pygame.transform.scale(Background_fig, (800, 600))  # Ajusta para 800x600
        self.image = Background_fig  # Atribui a imagem ao atributo da classe

        # Carrega e ajusta as margens laterais
        margin_left_fig = pygame.image.load("Images/margin_1.png")
        margin_left_fig = margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig, (60, 600))  # Ajuste para a altura correta
        self.margin_left = margin_left_fig

        margin_right_fig = pygame.image.load("Images/margin_2.png")
        margin_right_fig = margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (60, 600))  # Ajuste para a altura correta
        self.margin_right = margin_right_fig

    def update(self, dt):
        pass  # Aqui você pode adicionar lógica para atualizar o plano de fundo, se necessário

    def draw(self, screen):
        screen.blit(self.image, (0, 0))  # Desenha a imagem do fundo na tela
        screen.blit(self.margin_left, (0, 0))  # Desenha a margem esquerda
        screen.blit(self.margin_right, (740, 0))  # Desenha a margem direita

    def move(self, screen, scr_height, movL_y, movR_y):
        """
        Método para mover as margens e o plano de fundo de forma contínua.
        """
        # Movimento contínuo do fundo
        screen.blit(self.image, (0, movL_y))
        screen.blit(self.image, (0, movL_y - scr_height))  # Desenha de novo para cobrir todo o fundo

        # Desenha as margens com movimento contínuo
        screen.blit(self.margin_left, (0, movL_y))
        screen.blit(self.margin_left, (0, movL_y - scr_height))  # Desenha de novo para cobrir todo o fundo

        screen.blit(self.margin_right, (740, movR_y))
        screen.blit(self.margin_right, (740, movR_y - scr_height))  # Desenha de novo para cobrir todo o fundo
