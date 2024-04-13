import pygame
from scenes.game import Map, Camera
from config.settings import Settings
from entities.Player import Player

def run_game():
    FPS = 60
    pygame.init()
    pygame.display.set_caption("FUND")
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    # Configurações do mapa
    MAP_WIDTH, MAP_HEIGHT = 12800, 640
    game_map1 = Map('scenes/mapa1.csv')  # Substitua pelo caminho correto do arquivo CSV
    game_map1.set_background('assets/Background/backgroundF1.png')

    # Cria a câmera
    camera = Camera(MAP_WIDTH, MAP_HEIGHT, game_settings.screen_width, game_settings.screen_height)

    player = Player(400, 600, 32, 32, velocidade=10)  # Ajuste os parâmetros conforme necessário

    # Loop principal do jogo
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        # Atualizações do jogador
        player.loop(FPS, game_map1)

        # Obtém as teclas pressionadas
        keys = pygame.key.get_pressed()
        # Atualiza os deslocamentos com base nas teclas pressionadas
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left()  # Atualiza a velocidade do jogador para esquerda
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_right()  # Atualiza a velocidade do jogador para direita

        # Atualiza a câmera com base na velocidade do jogador
        camera.camera.x += player.x_vel

        player.update()  # Atualiza o jogador
        game_map1.draw(screen, camera)  # Desenha o mapa e o fundo deslocados pela câmera
        player.draw(screen, player.rect.x - camera.camera.x)  # Desenha o jogador com ajuste de câmera
        camera.update()  # Atualiza a câmera para o mapa não sair da tela
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    run_game()
