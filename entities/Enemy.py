#Enemy
import pygame
from utils.Imports import Imports

class Enemy(pygame.sprite.Sprite):
    ANIMATION_DELAY = 2
    def __init__(self, x, y, width, screen, player, game_map, spawn_x, move_range):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, width)
        self.x_vel = 2  # Velocidade horizontal inicial
        self.y_vel = 0
        self.direction = "right"
        self.animation_count = 0
        self.velocidade = 2
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

    def load_sprites(self):
        # Carrega os sprites do inimigo
        self.SPRITES = Imports().load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)

    def update(self):
        # Atualiza a posição horizontal do inimigo
        self.rect.x += self.x_vel

        # Verifica se o inimigo atingiu os limites de movimento
        if self.rect.left < self.min_x:
            self.rect.left = self.min_x
            self.x_vel = -self.x_vel  # Inverte a direção para a direita
            self.direction = "right"
        elif self.rect.right > self.max_x:
            self.rect.right = self.max_x
            self.x_vel = -self.x_vel  # Inverte a direção para a esquerda
            self.direction = "left"

        self.update_sprite()

    def check_collision_with_ground(self):
        future_rect = self.rect.copy()
        future_rect.y += self.y_vel

        # Verifica colisão com o chão (tiles sólidos)
        if self.game_map.check_collision(future_rect):
            # Muda a direção se bater em uma parede
            self.x_vel = -self.x_vel

    def update_sprite(self):
        sprite_sheet_name = "run_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

    def draw(self, screen):
        self.screen.blit(self.sprite, self.rect)
