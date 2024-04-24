#main
import pygame

from entities.Enemy import Capivara, Carro, Boss, Book, Zombie
from scenes.LifeCounter import LifeCounter
from scenes.game import Map, Camera
from config.settings import Settings
from entities.Player import BoyPlayer, GirlPlayer, SapoNinja
import pygame.mixer


def run_game(personagem, screen):
    #pygame.init()
    #pygame.display.set_caption("FUND")

    pygame.mixer.init()
    pygame.mixer.music.load('assets\Music/SubwaySurfers.mp3')

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

    #Musica do jogo:
    pygame.mixer.music.play(-1)  # O argumento -1 faz com que a música se repita continuamente

    enemy_list = []  # Lista para armazenar os inimigos
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
                #spawn_x = 400  # Posição inicial do inimigo no eixo X
                #move_range = 200  # Intervalo de movimento permitido (em pixels)

                fase1_inimigos = [
                    (1000, 2000, Carro),
                    (400, 400, Capivara),
                    (1800, 400, Capivara),
                    (2500, 400, Capivara),
                    (3500, 400, Capivara),
                    (4500, 400, Capivara),
                    (5500, 400, Capivara),
                    (3000, 2000, Carro),
                    (7500, 400, Capivara),
                    (8500, 400, Capivara),
                    (9500, 400, Capivara),
                    (5000, 2000, Carro),
                    (7000, 2000, Carro),
                    (9000, 2000, Carro),
                    (10500, 400, Capivara),
                    (11500, 400, Capivara)
                ]

                enemy_group = pygame.sprite.Group()  # Grupo para os inimigos
                for spawn_x, move_range, enemy_type in fase1_inimigos:

                    if enemy_type == Carro:
                        enemy_y = 400  # Coordenada Y para o tipo Carro
                    elif enemy_type == Capivara:
                        enemy_y = 520  # Coordenada Y para o tipo Capivara

                    enemy = enemy_type(spawn_x, enemy_y, 200, screen, player, game_maps[current_level - 1], spawn_x,
                                       move_range)
                    enemy_group.add(enemy)  # Adiciona o inimigo ao grupo
                    enemy_list.append(enemy)  # Adiciona o inimigo à lista

            if ( current_level == 1 and player.rect.x >= MAP_WIDTH - 700): #se chegar no final do nivel 1 passa pro nivel 2
                enemy_list = []
                current_level += 1
                camera.show_level_transition_screen(screen, current_level, 'Volte ao FUND, tem um exame te esperando')
                
                player.rect.x =  MAP_WIDTH-400  # Reset player position
                camera.camera.x =  MAP_WIDTH-400 # Reset camera position


                # Lista de dados dos inimigos a serem criados
                enemies_data = [

                    (500, 400, 200, Capivara),  # (spawn_x, move_range, enemy_type)
                    (800, 2000, 200, Capivara),
                    (1200, 2000, 200, Capivara),
                    (1600, 2000, 200, Capivara),
                    (2000, 2000, 200, Capivara),
                    (2500, 2000, 200, Capivara),
                    (3400, 2000, 200, Capivara),
                    (4400, 2000, 200, Capivara),
                    (5400, 2000, 200, Capivara),
                    (6400, 2000, 200, Capivara),
                    (7400, 2000, 200, Capivara),
                    (8400, 2000, 200, Capivara),
                    (9400, 2000, 200, Capivara),
                    (10400, 2000, 200, Capivara),
                    (11400, 2000, 200, Capivara),
                    (3400, 2000, 200, Capivara),
                    (5000, 200, 200, Capivara),
                    (1000, 2000, 200, Carro),
                    (3000, 2000, 200, Carro),
                    (5000, 2000, 200, Carro),
                    (5000, 2000, 200, Carro),
                    (6000, 2000, 200, Carro),
                    (8000, 2000, 200, Carro),
                    (10000, 2000, 200, Carro),

                ]

                enemy_group = pygame.sprite.Group()  # Grupo para os inimigos

                # Iterar sobre a lista de dados dos inimigos
                for spawn_x, move_range, size, enemy_type in enemies_data:
                    enemy = enemy_type(spawn_x, 520 if enemy_type == Capivara else 400, size, screen, player,
                                       game_maps[current_level - 1], spawn_x, move_range)
                    enemy_group.add(enemy)  # Adicionar o inimigo ao grupo
                    enemy_list.append(enemy)  # Adiciona o inimigo à lista

            if ( current_level == 2 and player.rect.x <= 200): #se chegar no inicio do nivel 2 passa pro nivel 3
                enemy_list = []
                current_level += 1
                camera.show_level_transition_screen(screen, current_level, 'Encontre o exame no final do corredor')
                player.rect.x =  0  # Reset player position
                camera.camera.x =  0 # Reset camera position

                # Cria o inimigo da fase

                # Lista de dados dos inimigos a serem criados
                enemies_data = [
                    (MAP_WIDTH - 1500, 300, 350, Book),  # (spawn_x, move_range, size, enemy_type)
                    (MAP_WIDTH - 300, 300, 270, Boss),
                    (MAP_WIDTH - 3000, 300, 350, Zombie),
                    (MAP_WIDTH - 4000, 300, 350, Zombie)
                ]

                enemy_group = pygame.sprite.Group()  # Grupo para os inimigos

                # Iterar sobre a lista de dados dos inimigos
                for spawn_x, move_range, size, enemy_type in enemies_data:
                    enemy = enemy_type(spawn_x, 350, size, screen, player, game_maps[current_level - 1], spawn_x,
                                       move_range)
                    enemy_group.add(enemy)  # Adicionar o inimigo ao grupo
                    enemy_list.append(enemy)  # Adiciona o inimigo à lista

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

            # Desenhar e atualizar todos os inimigos na lista
            for enemy in enemy_list:
                enemy.draw(camera)  # Desenha o inimigo na tela
                enemy.update()  # Atualiza o inimigo

            life_counter.draw_hearts(screen)  # Desenha os corações cheios e vazios

            #Adicionar colisao

            if pygame.sprite.spritecollide(player, enemy_group, False):
                player.make_hit()
                if life_counter.hit_cooldown ==0 :#game_settings.fps *2:
                    life_counter.perder_vida()  # Reduz o número de vidas restantes do jogador

            life_counter.update()

        pygame.display.flip()
    pygame.quit()


