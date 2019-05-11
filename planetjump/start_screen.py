import pygame

from planetjump.utils import load_image, terminate


class StartScreen:
    def __init__(self, surface):
        self.surface = surface
        self.background = load_image("start_background.png")
        self.start = False
        self.logo = load_image("logo.png")
        play = load_image("play.png")
        self.play_images = [(play, (118, 300)),
                            (pygame.transform.scale(play, (170, 80)), (115, 298))]
        self.play = self.play_images[0]

    def run(self):
        while not self.start:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.mouse_handler()
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.logo, (57, 100))
        self.surface.blit(self.play[0], self.play[1])
        pygame.display.flip()

    def mouse_handler(self):
        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if pygame.Rect(*self.play[1], *self.play[0].get_rect().size).collidepoint(*pos):
            self.play = self.play_images[1]
            if mouse_pressed:
                self.start = True
        else:
            self.play = self.play_images[0]
