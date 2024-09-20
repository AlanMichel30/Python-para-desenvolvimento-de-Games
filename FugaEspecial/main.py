import pygame
from Background import Background  # Importa o background

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None

    def __init__(self, size, fullscreen):
        pygame.init()

        # Define o tamanho da tela e o modo de exibição
        self.screen = pygame.display.set_mode((self.width, self.height))  
        self.screen_size = self.screen.get_size()  # Definir o tamanho da tela do jogo

        pygame.mouse.set_visible(False)  # Ocultar o cursor
        pygame.display.set_caption('Fuga Especial')  # Título da janela

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False  # Trata a saída do jogo

    def elements_update(self, dt):
        if self.background:
            self.background.update(dt)  # Atualiza o fundo

    def elements_draw(self):
        if self.background:
            self.background.draw(self.screen)  # Desenha o fundo

    def loop(self):
        """
        Laço principal do jogo
        """
        self.background = Background()  # Cria o plano de fundo

        clock = pygame.time.Clock()  # Inicializa o relógio
        dt = 16  # Tempo entre atualizações

        # Início do loop principal do programa
        while self.run:
            clock.tick(60)  # Limita o FPS a 60 quadros por segundo

            self.handle_events()  # Trata eventos do jogo
            self.elements_update(dt)  # Atualiza os elementos do jogo
            self.elements_draw()  # Desenha os elementos na tela

            pygame.display.update()  # Atualiza a tela

        pygame.quit()  # Fecha o Pygame ao terminar

# Iniciar o jogo
if __name__ == "__main__":
    game = Game("resolution", "fullscreen")  # Instanciar o objeto jogo
    game.loop()  # Iniciar o jogo
