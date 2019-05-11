import pygame
from .other import load_image, terminate
from .player import Player
from .platform import Platform
from .pause_screen import PauseScreen


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.backgrounds = [[load_image("background.png"), (0, 0)],
                            [load_image("background.png"), (0, -800)]]
        self.game = True
        self.pause = False
        self.all_sprites = pygame.sprite.Group()
        self.platforms = [Platform(self, self.surface, y) for y in range(0, 800, 100)]
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

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.set_pause()

    def update(self):
        self.background_scrolling()
        self.surface.blit(self.backgrounds[0][0], self.backgrounds[0][1])
        self.surface.blit(self.backgrounds[1][0], self.backgrounds[1][1])
        self.all_sprites.draw(self.surface)
        self.player.update()
        for platform in self.platforms:
            platform.update()
        pygame.display.flip()

    def background_scrolling(self):
        if self.backgrounds[0][1][1] <= 800:
            self.backgrounds[0][1] = self.backgrounds[0][1][0], self.backgrounds[0][1][1] + 1
            self.backgrounds[1][1] = self.backgrounds[1][1][0], self.backgrounds[1][1][1] + 1

        else:
            self.backgrounds = [[load_image("background.png"), (0, 0)],
                                [load_image("background.png"), (0, -800)]]

    def set_pause(self):
        self.pause = True
        PauseScreen(self)