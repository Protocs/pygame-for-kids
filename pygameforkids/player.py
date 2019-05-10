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

    def update(self):
        self.rect.y -= 2

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 1