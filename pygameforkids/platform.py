import pygame
from random import randint

from .other import load_image

class Platform(pygame.sprite.Sprite):
    def __init__(self, game, surface, y):
        super().__init__(game.all_sprites)
        self.surface = surface
        self.image = load_image("platform.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 323)
        self.rect.y = y

    def update(self):
        self.rect.y += 2