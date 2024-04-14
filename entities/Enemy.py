#Enemy
import pygame
from utils.Imports import Imports

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, distance, screen, player, game_map):
        super(Enemy, self).__init__()
        self.screen = screen
        self.player = player
        self.game_map = game_map

        # Define the initial position of the enemy
        self.rect = pygame.Rect(x, y, 32, 32)

        # Adjust enemy's position to be on solid ground
        self.adjust_position_to_ground()

        # Define movement boundaries for the enemy
        self.start_x = self.rect.x
        self.end_x = self.rect.x + distance
        self.direction = 1  # Start moving right initially
        self.velocidade = 2  # Movement speed of the enemy

        # Load enemy sprites
        self.SPRITES = Imports().load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
        self.sprite_sheet = "run"
        self.animation_count = 0
        self.image = None

    def adjust_position_to_ground(self):
        """Adjusts the enemy's position to be on solid ground."""
        tile_size = 32
        x_tile = self.rect.centerx // tile_size
        y_tile = self.rect.bottom // tile_size

        # Find the nearest solid ground below the enemy's initial position
        while not self.game_map.is_tile_solid(x_tile, y_tile):
            y_tile += 1

        # Set the enemy's position to the top of the solid ground tile
        self.rect.bottom = y_tile * tile_size

    def update(self):
        # Update the enemy's position based on the current direction
        self.rect.x += self.direction * self.velocidade

        # Check if the enemy has reached its movement boundaries
        if self.rect.x <= self.start_x or self.rect.x >= self.end_x:
            self.direction *= -1  # Reverse the direction

        # Check collision with the player
        if pygame.sprite.collide_rect(self, self.player):
            self.player.make_hit()  # Cause damage to the player
            self.player.hit = True  # Set player's hit status to true

        # Update the enemy's sprite animation
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet_name = self.sprite_sheet
        if sprite_sheet_name in self.SPRITES:
            sprites = self.SPRITES[sprite_sheet_name]
            sprite_index = (self.animation_count // 2) % len(sprites)
            self.image = sprites[sprite_index]
            self.animation_count += 1

    def draw(self):
        if self.image is not None:
            self.screen.blit(self.image, self.rect)

    def set_position(self, x, y):
        # Set the enemy's position
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.end_x = x + (self.end_x - self.start_x)  # Maintain the same movement range relative to the new start position
