import pygame

from planetjump.utils import load_best_progress


class BestScore(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.font = pygame.font.Font("data/fonts/PressStart2P.ttf", 16)
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.color = (251, 32, 122)
        self.rect.x = 200
        self.rect.y = 220
        self.score = load_best_progress()

    def update(self):
        self.image = self.font.render("Best: " + str(self.score), True, self.color)


class Score(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game.score_group)
        self.game = game
        self.font = pygame.font.Font("data/fonts/PressStart2P.ttf", 16)
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 15
        self.color = (251, 32, 122)

    def update(self):
        self.image = self.font.render("Score: " + str(self.game.player.score), True, self.color)
