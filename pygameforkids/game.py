import pygame
from .other import load_image, terminate


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = load_image("background.png")
        self.game = True

    def run(self):
        while self.game:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.surface.blit(self.background, (0, 0))
        pygame.display.flip()
