import pygame

from planetjump.utils import load_image, load_best_progress, save_progress
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
        self.score = 0
        self.best_score = load_best_progress()

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
            if self.rect.y >= 380:
                self.rect.y -= self.speeding
                if self.game.start_pos:
                    self.score += 1
            elif self.rect.y < 380:
                self.score += 1
            self.speeding -= 0.06
        else:
            self.moving = False

        if not self.moving:
            self.speeding += 0.1
            self.rect.y += round(self.speeding)

    def key_handle(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 4
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 4

    def find_collide(self):
        if self.moving:
            return

        for sprite in self.game.all_sprites:
            if pygame.sprite.collide_mask(self, sprite) and sprite != self:
                if self.rect.y + 40 <= sprite.rect.y:
                    self.speeding = 5
                    self.moving = True

                    if sprite == self.game.platforms[-1]:
                        sprite.rect.y -= 900

    def death(self):
        try:
            if self.score > self.best_score:
                save_progress(self.score)
        except:
            save_progress(self.score)

        self.game.score_counter.rect.x = (400 - self.game.score_counter.rect.width) / 2
        self.game.score_counter.rect.y = 200
        DeathScreen(self.surface, self.game.score_group, self.game.score_counter)
