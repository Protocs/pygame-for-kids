import pygame

from planetjump.background import Background
from planetjump.utils import handle_close
from planetjump.player import Player
from planetjump.platform import Platform
from planetjump.pause_screen import PauseScreen
from planetjump.disappearing_platform import DisappearingPlatform
from planetjump.score import Score


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.backgrounds = [Background(0, 0), Background(0, -800)]
        self.game = True
        self.pause = False
        self.all_sprites = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()
        self.platforms = [Platform(self, self.surface, y) for y in range(100, 800, 100)]
        self.platforms.append(DisappearingPlatform(self, self.surface, 0))
        self.player = Player(self, self.surface)
        self.clock = pygame.time.Clock()
        self.score_counter = Score(self)
        self.start_pos = True

    def run(self):
        while self.game:
            self.events()
            self.update()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            handle_close(event)

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.set_pause()

    def update(self):
        if self.player.rect.y <= 380 and self.player.moving:
            self.background_scrolling(self.player.speeding / 2)
        self.draw_backgrounds()
        self.all_sprites.draw(self.surface)
        self.player.update()
        self.score_group.draw(self.surface)
        self.score_counter.update()
        for platform in self.platforms:
            platform.update()
        pygame.display.flip()

    def draw_backgrounds(self):
        first_bg, second_bg = self.backgrounds
        self.surface.blit(first_bg.image, tuple(first_bg.point))
        self.surface.blit(second_bg.image, tuple(second_bg.point))

    def background_scrolling(self, dy):
        first_bg, second_bg = self.backgrounds
        self.start_pos = False
        if first_bg.point.y <= 800:
            first_bg.point.y += dy
            second_bg.point.y += dy
        else:
            self.backgrounds = [Background(0, 0), Background(0, -800)]

    def set_pause(self):
        self.pause = True
        PauseScreen(self)

