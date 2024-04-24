#Enemy
import pygame
from utils.Imports import Imports

class Enemy(pygame.sprite.Sprite):
    ANIMATION_DELAY = 3
    SPEED = 2  # Velocidade constante do inimigo

    def __init__(self, x, y, width, screen, player, game_map, spawn_x, move_range):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, width)
        self.direction = "right"
        self.animation_count = 0
        self.screen = screen
        self.player = player
        self.game_map = game_map
        self.spawn_x = spawn_x  # Posição inicial do inimigo no eixo X
        self.move_range = move_range  # Intervalo de movimento permitido (em pixels)

        # Definir os limites de movimento do inimigo
        self.min_x = self.spawn_x - self.move_range  # Limite esquerdo do movimento
        self.max_x = self.spawn_x + self.move_range  # Limite direito do movimento

        self.load_sprites()
        self.update_sprite()

    def update(self):
        # Atualiza a posição horizontal do inimigo com velocidade constante
        if self.direction == "right":
            self.rect.x += self.SPEED
        else:
            self.rect.x -= self.SPEED

        # Verifica se o inimigo atingiu os limites de movimento
        if self.rect.left < self.min_x:
            self.rect.left = self.min_x
            self.direction = "right"  # Inverte a direção para a direita
        elif self.rect.right > self.max_x:
            self.rect.right = self.max_x
            self.direction = "left"  # Inverte a direção para a esquerda

        self.update_sprite()

    def update_sprite(self):
        sprite_sheet_name = "run_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

    def draw(self, camera):
        # Calcula a posição relativa ao cenário de fundo
        relative_position = self.rect.x - camera.camera.x

        # Desenha o sprite do inimigo na posição relativa
        self.screen.blit(self.sprite, (relative_position, self.rect.y))

class Capivara(Enemy):
    def __init__(self, x, y, width, screen, player, game_map, spawn_x, move_range):
        super().__init__(x, y, width, screen, player, game_map, spawn_x, move_range)
        self.load_sprites()

    def load_sprites(self):
        # Carrega os sprites da menina
        self.SPRITES = Imports().load_sprite_sheets("MainCharacters", "capivara", 64, 96, True)


class Carro(Enemy):
    def __init__(self, x, y, width, screen, player, game_map, spawn_x, move_range):
        super().__init__(x, y, width, screen, player, game_map, spawn_x, move_range)
        self.load_sprites()

    def load_sprites(self):
        # Carrega os sprites do menino
        self.SPRITES = Imports().load_sprite_sheets("items", "jeep_2", 256, 96, True)

class Boss(Enemy):
    def __init__(self, x, y, width, screen, player, game_map, spawn_x, move_range):
        super().__init__(x, y, width, screen, player, game_map, spawn_x, move_range)
        self.load_sprites()

    def load_sprites(self):
        # Carrega os sprites do menino
        self.SPRITES = Imports().load_sprite_sheets("MainCharacters", "boss", 128, 150, True)

class Book(Enemy):
    def __init__(self, x, y, width, screen, player, game_map, spawn_x, move_range):
        super().__init__(x, y, width, screen, player, game_map, spawn_x, move_range)
        self.load_sprites()

    def load_sprites(self):
        # Carrega os sprites do menino
        self.SPRITES = Imports().load_sprite_sheets("MainCharacters", "book", 90, 110, True)

class Zombie(Enemy):
    def __init__(self, x, y, width, screen, player, game_map, spawn_x, move_range):
        super().__init__(x, y, width, screen, player, game_map, spawn_x, move_range)
        self.load_sprites()

    def load_sprites(self):
        # Carrega os sprites do menino
        self.SPRITES = Imports().load_sprite_sheets("MainCharacters", "Zombie", 86,100 , True)