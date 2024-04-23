#main
import pygame

from entities.Enemy import Capivara, Carro, Boss, Book
from scenes.LifeCounter import LifeCounter
from scenes.game import Map, Camera
from config.settings import Settings
from entities.Player import BoyPlayer, GirlPlayer, SapoNinja


def run_game(personagem, screen):
    #pygame.init()
    #pygame.display.set_caption("FUND")

    game_settings = Settings()
    #screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    # Configurações do mapa
    MAP_WIDTH, MAP_HEIGHT = 12800, 640
    background_images = ['assets/Background/backgroundF1.png', 'assets/Background/backgroundF2.png', 'assets/Background/backgroundF3.png']
    game_maps = [Map('scenes/mapa1.csv'), Map('scenes/mapa2.csv'), Map('scenes/mapa3.csv')]
    # Itera sobre ambas as listas juntas usando zip
    for game_map, bg_image in zip(game_maps, background_images):
        game_map.set_background(bg_image)

    # Cria a câmera
    camera = Camera(MAP_WIDTH, MAP_HEIGHT, game_settings.screen_width, game_settings.screen_height)

    # Cria o player
    if( personagem == 1):
        player= BoyPlayer(100, 100, 50, 50, velocidade=10)
    if(personagem ==2):
        player= GirlPlayer(100, 100, 50, 50, velocidade=10)
    if (personagem == 3):
        player = SapoNinja(100, 100, 50, 50, velocidade=30)

    # Loop do jogo
    clock = pygame.time.Clock()
    run = True
    paused = False
    current_level = 1
    inicio = True

    # Inicializa o contador de vidas para o jogador
    life_counter = LifeCounter(player)  # Inicializa com 3 vidas


    while run:
        clock.tick(game_settings.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2 and not paused:
                    player.jump()
                if event.key == pygame.K_ESCAPE:  # Press 'p' to pause/unpause
                    paused = not paused
                    camera.pausado(screen)

        if not paused:

            # Verifica se o jogador ainda está vivo
            if not player.is_alive:
                space_pressed = camera.show_death_screen(screen)
                if space_pressed:
                    run_game(personagem, screen)  # Reinicia o jogo
                    return  # Sai do loop atual

            # Handle player input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.move_left()
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.move_right()
            else:
                player.stop_moving()

            if ( current_level == 1 and inicio ): #começo nivel 1
                inicio = False
                camera.show_level_transition_screen(screen, current_level, 'Você esqueceu a lista, volte ao H8A para pegar')
                # Cria o inimigo da fase
                spawn_x = 400  # Posição inicial do inimigo no eixo X
                move_range = 200  # Intervalo de movimento permitido (em pixels)

                # Cria o inimigo da fase
                spawn_x = 400  # Posição inicial do inimigo no eixo X
                move_range = 400  # Intervalo de movimento permitido (em pixels)
                enemy1 = Capivara(spawn_x, 520, 200, screen, player, game_maps[current_level-1], spawn_x, move_range)

                # Cria o inimigo da fase
                spawn_x = 1000  # Posição inicial do inimigo no eixo X
                move_range = 2000  # Intervalo de movimento permitido (em pixels)
                enemy2 = Carro(spawn_x, 400, 200, screen, player, game_maps[current_level-1], spawn_x, move_range)

                #auxiliar para colisão
                enemy_group = pygame.sprite.Group()  # Grupo para os inimigos
                enemy_group.add(enemy1, enemy2)  # Adiciona os inimigos ao grupo


            if ( current_level == 1 and player.rect.x >= MAP_WIDTH - 700): #se chegar no final do nivel 1 passa pro nivel 2
                current_level += 1
                camera.show_level_transition_screen(screen, current_level, 'Volte ao FUND, tem um exame te esperando')
                
                player.rect.x =  MAP_WIDTH-400  # Reset player position
                camera.camera.x =  MAP_WIDTH-400 # Reset camera position

                # Cria o inimigo da fase
                spawn_x = 5000  # Posição inicial do inimigo no eixo X
                move_range = 400  # Intervalo de movimento permitido (em pixels)
                enemy1 = Capivara(spawn_x, 520, 200, screen, player, game_maps[current_level-1], spawn_x, move_range)

                # Cria o inimigo da fase
                spawn_x = 5000  # Posição inicial do inimigo no eixo X
                move_range = 2000  # Intervalo de movimento permitido (em pixels)
                enemy2 = Carro(spawn_x, 400, 200, screen, player, game_maps[current_level-1], spawn_x, move_range)

                # auxiliar para colisão
                enemy_group = pygame.sprite.Group()  # Grupo para os inimigos
                enemy_group.add(enemy1, enemy2)  # Adiciona os inimigos ao grupo


            if ( current_level == 2 and player.rect.x <= 200): #se chegar no inicio do nivel 2 passa pro nivel 3
                current_level += 1
                camera.show_level_transition_screen(screen, current_level, 'Encontre o exame no final do corredor')
                player.rect.x =  0  # Reset player position
                camera.camera.x =  0 # Reset camera position

                # Cria o inimigo da fase

                spawn_x = MAP_WIDTH - 300  # Posição inicial do inimigo no eixo X
                move_range = 300  # Intervalo de movimento permitido (em pixels)
                enemy1 = Book(spawn_x, 270, 200, screen, player, game_maps[current_level - 1], spawn_x, move_range)

                spawn_x = MAP_WIDTH - 300  # Posição inicial do inimigo no eixo X
                move_range = 300  # Intervalo de movimento permitido (em pixels)
                enemy2 = Boss(spawn_x, 270, 200, screen, player, game_maps[current_level-1], spawn_x, move_range)

                # auxiliar para colisão
                enemy_group = pygame.sprite.Group()  # Grupo para os inimigos
                enemy_group.add(enemy1, enemy2)  # Adiciona os inimigos ao grupo

            if ( current_level == 3 and player.rect.x >= MAP_WIDTH-200): #se chegar no final, vence
                current_level += 1
                camera.show_level_transition_screen(screen, current_level, 'Você concluiu o jogo')
            
            if current_level >= 4:  # If there are no more levels, end the game
                    run = False

            # Update player position and behavior
            player.loop(game_settings.fps, game_maps[current_level-1])

            # Update camera position
            camera.camera.x = player.rect.centerx - camera.width / 2
            camera.camera.y = player.rect.centery - camera.height / 2
            camera.camera.x = max(0, min(camera.camera.x, MAP_WIDTH - camera.width))
            camera.camera.y = max(0, min(camera.camera.y, MAP_HEIGHT - camera.height))

            # Dentro do loop principal do jogo
            game_maps[current_level-1].draw(screen, camera)  # Desenha o mapa na tela
            player.draw(screen, camera.camera.x)  # Desenha o jogador na tela
            enemy1.draw(camera)  # Desenha o inimigo na tela
            enemy2.draw(camera)

            life_counter.draw_hearts(screen)  # Desenha os corações cheios e vazios

            # Update and draw the enemy
            enemy1.update()  
            enemy2.update()

            #Adicionar colisao

            if pygame.sprite.spritecollide(player, enemy_group, False):
                player.make_hit()
                if life_counter.hit_cooldown ==0 :#game_settings.fps *2:
                    life_counter.perder_vida()  # Reduz o número de vidas restantes do jogador

            life_counter.update()

        pygame.display.flip()
    pygame.quit()


