# mainmenu.py
import pygame
import pygame_menu
from principal import run_game

class MainMenu:
    def __init__(self, width, height):
        super(). __init__()
        pygame.init()
        pygame.display.set_caption("FUND")
        self.surface = pygame.display.set_mode((width,height))
        self.menu = pygame_menu.Menu( 'Main Menu', width,height, theme=pygame_menu.themes.THEME_BLUE)
        self.character = 1
        self.width=width
        self.height=height
        self.menu.add.selector('Choose character: ', [('Bixo', 1), ('Bixete', 2),('Sapo Ninja', 3)], onchange=self.set_character)
        self.menu.add.button('Start Game', self.start_game)
        self.menu.add.button('Settings', self.settings)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def set_character(self, value, index):
        self.character = index
        print(index)

    def start_game(self):
        while True:
            run_game(self.character, self.surface)
            # Aguarda o jogo terminar para retornar ao menu principal
            self.menu.mainloop(self.surface)  # Mostra o menu principal novamente
    def settings(self):
        print('Opening settings')

    def main_loop(self):
        self.menu.mainloop(self.surface)

    def pausado(self):
        font = pygame.font.Font(None, 74)  # Escolha a fonte para renderizar o texto
        text = font.render('Pausado', True, (255, 255, 255))  # Renderiza o texto
        text_rect = text.get_rect(center=(self.width/2,self.height/2))  # Centraliza o texto
        s = pygame.Surface((self.width,self.height))  # Cria uma nova superfície
        s.set_alpha(128)  # Define o nível de transparência (0-255, 0 é totalmente transparente)
        s.fill((128,128,128))  # Preenche a superfície com cinza
        self.surface.blit(s, (0,0))  # Desenha a superfície na tela
        self.surface.blit(text, text_rect)



