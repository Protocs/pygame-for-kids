from random import randint

import pygame

from planetjump.utils import load_image


class Platform(pygame.sprite.Sprite):
    def __init__(self, game, surface, y):
        super().__init__(game.all_sprites)
        self.game = game
        self.surface = surface
        self.image = load_image("platform.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 323)
        self.rect.y = y

    def update(self):
        if self.rect.y <= 800:
            if self.game.player.rect.y < 380:
                self.rect.y += self.game.player.speeding
        else:
            self.rect.y = -16
            self.rect.x = randint(0, 323)
