#main
import pygame

from entities.Enemy import Enemy
from scenes.game import Map, Camera
from config.settings import Settings
from entities.Player import Player

def run_game():
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

    # Cria o player
    player = Player(100, 100, 50, 50, velocidade=10)

    # Cria o inimigo
    enemy = Enemy(500, 100, 200, screen, player, game_map1)

    # Loop do jogo
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(game_settings.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_right()
        else:
            player.stop_moving()

        if keys[pygame.K_SPACE]:
            player.jump()

        # Update player position and behavior
        player.loop(game_settings.fps, game_map1)

        # Update camera position
        camera.camera.x = player.rect.centerx - camera.width / 2
        camera.camera.y = player.rect.centery - camera.height / 2
        camera.camera.x = max(0, min(camera.camera.x, MAP_WIDTH - camera.width))
        camera.camera.y = max(0, min(camera.camera.y, MAP_HEIGHT - camera.height))

        # Clear screen
        screen.fill((0, 0, 0))

        # Dentro do loop principal do jogo
        game_map1.draw(screen, camera)  # Desenha o mapa na tela
        player.draw(screen, camera.camera.x)  # Desenha o jogador na tela
        enemy.draw()  # Desenha o inimigo na tela

        # Update and draw the enemy
        enemy.update()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    run_game()