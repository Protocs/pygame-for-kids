import pygame
from .other import load_image, terminate, SIZE

class StartScreen:
    def __init__(self, surface):
        self.surface = surface
        self.background = load_image("start_background.png")
        self.play_button = load_image("play.png")
        self.start = False

    def run(self):
        while True:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def update(self):
        self.surface.blit(self.background, (0, 0))
        self.background.blit(self.play_button, ((SIZE[0] - self.play_button.get_width()) / 2, 300))
        pygame.display.flip()