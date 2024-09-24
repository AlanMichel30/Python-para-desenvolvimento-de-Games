import pygame
from Background import Background  # Importa o background
from Player import Player  # Importa o Player

class Game:
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None
    player = None

    # movimento do Player
    DIREITA = pygame.K_RIGHT
    ESQUERDA = pygame.K_LEFT
    mudar_x = 0.0

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

        # se clicar em qualquer tecla, entra no if
            if event.type == pygame.KEYDOWN:
                if event.key == self.ESQUERDA: # se clicar na seta dda esquerda, anda 3 para a esperda no eixo x
                    self.mudar_x = -3
                if event.key == self.DIREITA: # se clicar ma seta da direita, anda 3 para a direita no eixo x
                    self.mudar_x = 3 

                if event.type == pygame.KEYUP:  # se soltar qualquer tecla, não faz nada
                    if event.key == self.ESQUERDA or event.key == self.DIREITA:
                        self.mudar_x = 0              

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
        # Velocidade de movimento do plano de fundo/margens
        velocidade_background = 5 
        
        # Movimento das margens e do fundo
        movL_y = 0
        movR_y = 0
        
        self.background = Background()  # Cria o plano de fundo

        # Posição inicial do Player 
        x = (self.width - 56) / 2
        y = self.height - 125

        # Criar o Player
        self.player = Player(x, y)

        clock = pygame.time.Clock()  # Inicializa o relógio
        dt = 16  # Tempo entre atualizações

        # Início do loop principal do programa
        while self.run:
            clock.tick(60)  # Limita o FPS a 60 quadros por segundo

            # Adiciona movimento ao background 
            self.background.move(self.screen, self.height, movL_y, movR_y)
            movL_y += velocidade_background
            movR_y += velocidade_background

            # Se a imagem ultrapassar a extremidade da tela, move de volta
            if movL_y > 600:
                movL_y = 0
            if movR_y > 600:
                movR_y = 0

            # Movimentação do Player
            # Altera a coordenada x da nave de acordo comas mudanças no event_handle() para ela se mover
            x = x + self.mudar_x    
            
            # Desenhar Player
            self.player.draw(self.screen, x, y)    
                
            self.handle_events()  # Trata eventos do jogo
            self.elements_update(dt)  # Atualiza os elementos do jogo
            self.elements_draw()  # Desenha os elementos na tela

            pygame.display.update()  # Atualiza a tela

        pygame.quit()  # Fecha o Pygame ao terminar

# Iniciar o jogo
if __name__ == "__main__":
    game = Game("resolution", "fullscreen")  # Instanciar o objeto jogo
    game.loop()  # Iniciar o jogo
