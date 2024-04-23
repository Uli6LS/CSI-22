import pygame

class LifeCounter:
    def __init__(self, player):
        self.max_lives = player.max_hits  # Número máximo de vidas é igual ao número máximo de hits do jogador
        self.current_lives = player.max_hits  # Número atual de vidas é inicializado como o máximo

        # Carrega os sprites para representar os corações
        self.full_heart = pygame.image.load('assets/Items/LifeCounter/coracao_cheio.png').convert_alpha()
        self.empty_heart = pygame.image.load('assets/Items/LifeCounter/coracao_vazio.png').convert_alpha()

        # Lista para armazenar o estado atual dos corações
        self.hearts = [True] * self.max_lives  # Inicialmente todos os corações estão cheios

    def perder_vida(self, hit):
        if hit:  # Usa diretamente o parâmetro hit
            # Verifica se ainda há vidas restantes antes de subtrair
            if self.current_lives > 0:
                self.hearts[self.current_lives - 1] = False
                self.current_lives -= 1

    def draw_hearts(self, screen):
        heart_width = self.full_heart.get_width()  # Largura de cada coração
        x = 10  # Posição inicial para desenhar os corações

        # Desenha os corações com base no estado atual da lista hearts
        for i, heart in enumerate(self.hearts):
            if heart:
                # Desenha coração cheio se o coração estiver True (cheio)
                screen.blit(self.full_heart, (x, 10))
            else:
                # Desenha coração vazio se o coração estiver False (vazio)
                screen.blit(self.empty_heart, (x, 10))

            x += heart_width + 5  # Incrementa a posição para o próximo coração

        # Desenha o texto com o número de vidas restantes
        font = pygame.font.Font(None, 36)
        text = font.render(f'Vidas Restantes: {self.current_lives}', True, (255, 255, 255))
        screen.blit(text, (x + 20, 10))  # Posiciona o texto ao lado dos corações
