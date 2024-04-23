import pygame

class LifeCounter:
    def __init__(self, initial_lives=3):
        self.max_lives = 3  # Sempre serão 3 espaços para corações
        self.vidas_restantes = initial_lives  # Vidas restantes do jogador
        self.alive = True

        # Carrega os sprites para representar os corações
        self.full_heart = pygame.image.load('assets/Items/LifeCounter/coracao_cheio.png').convert_alpha()
        self.empty_heart = pygame.image.load('assets/Items/LifeCounter/coracao_vazio.png').convert_alpha()

        # Lista para armazenar o estado atual dos corações
        self.hearts = [True] * self.max_lives  # Inicialmente todos os corações estão cheios

    def get_vidas_restantes(self):
        return self.vidas_restantes

    def perder_vida(self):
        if self.vidas_restantes > 0:
            # Marca o próximo coração como vazio
            self.hearts[self.vidas_restantes - 1] = False
            self.vidas_restantes -= 1
            if self.vidas_restantes == 0:
                self.alive = False

    def is_alive(self):
        return self.alive

    def draw(self, screen):
        heart_width = self.full_heart.get_width()  # Largura de cada coração
        x = 10  # Posição inicial para desenhar os corações

        # Desenha os três espaços de corações
        for i in range(self.max_lives):
            if self.hearts[i]:
                screen.blit(self.full_heart, (x, 10))  # Desenha coração cheio se o espaço estiver ocupado
            else:
                screen.blit(self.empty_heart, (x, 10))  # Desenha coração vazio se o espaço estiver vazio
            x += heart_width + 5  # Incrementa a posição para o próximo coração
