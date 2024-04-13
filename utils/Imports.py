#Imports
import os
import pygame

class Imports:
    def __init__(self):
        pass  # Constructor does not require parameters for this utility class

    @staticmethod
    def flip(sprites):
        """Flip sprites horizontally."""
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    @staticmethod
    def load_sprite_sheets(dir1, dir2, width, height, direction=False):
        """Load sprite sheets from specified directory."""
        path = os.path.join("assets", dir1, dir2)
        images = [f for f in os.listdir(path) if f.endswith('.png')]

        all_sprites = {}

        for image in images:
            sprite_sheet = pygame.image.load(os.path.join(path, image)).convert_alpha()
            sprites = []

            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = Imports.flip(sprites)
            else:
                all_sprites[image.replace(".png", "")] = sprites

        return all_sprites

    @staticmethod
    def handle_vertical_collision(player, objects, dy):
        """Handle vertical collision with objects."""
        collided_objects = []

        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hit_head()

                collided_objects.append(obj)

        return collided_objects

    @staticmethod
    def collide(player, objects, dx):
        """Check collision while moving horizontally."""
        player.move(dx, 0)
        player.update()
        collided_object = None

        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                collided_object = obj
                break

        player.move(-dx, 0)
        player.update()
        return collided_object

    @staticmethod
    def handle_move(player, objects, PLAYER_VEL):
        """Handle player movement based on keyboard input."""
        keys = pygame.key.get_pressed()

        player.x_vel = 0
        collide_left = Imports.collide(player, objects, -PLAYER_VEL * 2)
        collide_right = Imports.collide(player, objects, PLAYER_VEL * 2)

        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)

        vertical_collide = Imports.handle_vertical_collision(player, objects, player.y_vel)
        to_check = [collide_left, collide_right, *vertical_collide]

        for obj in to_check:
            if obj and obj.name == "fire":
                player.make_hit()
