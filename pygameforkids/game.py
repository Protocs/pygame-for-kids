import pygame
from .other import load_image, terminate
from .player import Player


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.backgrounds = [[load_image("background.png"), (0, 0)],
                            [load_image("background.png"), (0, -800)]]
        self.game = True
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self, self.surface)
        self.clock = pygame.time.Clock()

    def run(self):
        while self.game:
            self.events()
            self.update()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.background_scrolling()
        self.surface.blit(self.backgrounds[0][0], self.backgrounds[0][1])
        self.surface.blit(self.backgrounds[1][0], self.backgrounds[1][1])
        self.all_sprites.draw(self.surface)
        self.player.update()
        pygame.display.flip()

    def background_scrolling(self):
        self.backgrounds[0][1] = self.backgrounds[0][1][0], self.backgrounds[0][1][1] + 1
        self.backgrounds[1][1] = self.backgrounds[1][1][0], self.backgrounds[1][1][1] + 1
