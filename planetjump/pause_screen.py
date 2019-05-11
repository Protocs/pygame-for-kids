import pygame

from planetjump.utils import load_image, terminate
from planetjump.start_screen import StartScreen


class PauseScreen:
    def __init__(self, game):
        self.game = game
        self.surface = game.surface
        self.background = load_image("start_background.png")
        self.pause = load_image("pause.png")

        restart = load_image("restart.png")
        self.restart_images = [(restart, (118, 300)),
                               (pygame.transform.scale(restart, (170, 80)), (115, 298))]
        self.restart = self.restart_images[0]

        menu = load_image("menu.png")
        self.menu_images = [(menu, (118, 400)),
                            (pygame.transform.scale(menu, (170, 80)), (115, 398))]
        self.menu = self.menu_images[0]

        continue_button = load_image("continue.png")
        self.continue_images = [(continue_button, (118, 200)),
                                (pygame.transform.scale(continue_button, (170, 80)), (115, 198))]
        self.continue_button = self.continue_images[0]

        self.run()

    def run(self):
        while self.game.pause:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.mouse_handler()
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.pause, (0, 50))
        self.surface.blit(self.restart[0], self.restart[1])
        self.surface.blit(self.menu[0], self.menu[1])
        self.surface.blit(self.continue_button[0], self.continue_button[1])
        pygame.display.flip()

    def mouse_handler(self):
        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if pygame.Rect(*self.continue_button[1],
                       *self.continue_button[0].get_rect().size).collidepoint(*pos):
            self.continue_button = self.continue_images[1]
            if mouse_pressed:
                self.game.pause = False
        else:
            self.continue_button = self.continue_images[0]

        if pygame.Rect(*self.restart[1], *self.restart[0].get_rect().size).collidepoint(*pos):
            self.restart = self.restart_images[1]
            if mouse_pressed:
                self.game.__init__(self.surface)
        else:
            self.restart = self.restart_images[0]

        if pygame.Rect(*self.menu[1], *self.menu[0].get_rect().size).collidepoint(*pos):
            self.menu = self.menu_images[1]
            if mouse_pressed:
                start = StartScreen(self.surface)
                start.run()
                self.game.__init__(self.surface)
        else:
            self.menu = self.menu_images[0]
