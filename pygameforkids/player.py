import pygame

from .other import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, game, surface):
        super().__init__(game.all_sprites)
        self.surface = surface
        self.image = load_image("ball.png")
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 800
        self.speeding = 5
        self.moving = True

    def update(self):
        self.key_handle()

        if self.speeding > 0 and self.moving:
            self.rect.y -= round(self.speeding)
            self.speeding -= 0.03
        else:
            self.moving = False

        if not self.moving:
            self.speeding += 0.03
            self.rect.y += round(self.speeding)

    def key_handle(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 2

