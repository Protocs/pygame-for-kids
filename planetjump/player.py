import pygame

from planetjump.utils import load_image
from planetjump.death_screen import DeathScreen


class Player(pygame.sprite.Sprite):
    def __init__(self, game, surface):
        super().__init__(game.all_sprites)
        self.game = game
        self.surface = surface
        self.image = load_image("ball.png")
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 800
        self.speeding = 5
        self.moving = True

    def update(self):
        self.key_handle()
        self.find_collide()

        if self.rect.y >= 800 and not self.moving:
            self.death()
            self.game.__init__(self.surface)

        if self.rect.x <= -23:
            self.rect.x = 377

        elif self.rect.x >= 378:
            self.rect.x = -22

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
            self.rect.x -= 4
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 4

    def find_collide(self):
        pass

    def death(self):
        DeathScreen(self.surface)
