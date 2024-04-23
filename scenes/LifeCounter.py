import pygame

class LifeCounter:
    def __init__(self, player):
        self.max_lives = player.max_hits
        self.current_lives = player.max_hits
        self.full_heart = pygame.image.load('assets/Items/LifeCounter/coracao_cheio.png').convert_alpha()
        self.empty_heart = pygame.image.load('assets/Items/LifeCounter/coracao_vazio.png').convert_alpha()
        self.hearts = [True] * self.max_lives
        self.hit_cooldown = 0  # Cooldown period in milliseconds
        self.cooldown_period = 2000  # Cooldown period of 2 seconds (2000 milliseconds)

    def perder_vida(self):
        # Only lose a life if not in cooldown
        if self.current_lives > 0 and (pygame.time.get_ticks() - self.hit_cooldown >= self.cooldown_period or self.hit_cooldown == 0):
            self.hearts[self.current_lives - 1] = False
            self.current_lives -= 1
            self.hit_cooldown = pygame.time.get_ticks()  # Get the current time in milliseconds

    def update(self):
        # Decrease cooldown counter if it's greater than 0
        if self.hit_cooldown > 0:
            # Check if 2 seconds have passed since the last hit
            if pygame.time.get_ticks() - self.hit_cooldown >= self.cooldown_period:
                self.hit_cooldown = 0  # Reset cooldown

    def draw_hearts(self, screen):
        heart_width = self.full_heart.get_width()
        x = 10
        for i, heart in enumerate(self.hearts):
            if heart:
                screen.blit(self.full_heart, (x, 10))
            else:
                screen.blit(self.empty_heart, (x, 10))
            x += heart_width + 5
        font = pygame.font.Font(None, 36)
        text = font.render(f'Vidas Restantes: {self.current_lives}', True, (255, 255, 255))
        screen.blit(text, (x + 20, 10))

# No loop principal do jogo, certifique-se de chamar o método update do LifeCounter
# life_counter.update()

# A detecção de colisão deve ficar assim:
# if pygame.sprite.spritecollide(player, enemy_group, False):
#     player.make_hit()
#     life_counter.perder_vida()
