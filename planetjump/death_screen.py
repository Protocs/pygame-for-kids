import pygame

from .other import load_image, terminate

class DeathScreen:
    def __init__(self, surface):
        self.surface = surface
        self.background = load_image("start_background.png")
        self.death = True

        restart = load_image("restart.png")
        self.restart_images = [(restart, (118, 300)),
                            (pygame.transform.scale(restart, (170, 80)), (115, 298))]
        self.restart = self.restart_images[0]

        self.run()

    def run(self):
        while self.death:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.mouse_handler()
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.restart[0], self.restart[1])
        pygame.display.flip()

    def mouse_handler(self):
        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if pygame.Rect(*self.restart[1], *self.restart[0].get_rect().size).collidepoint(*pos):
            self.restart = self.restart_images[1]
            if mouse_pressed:
                self.death = False
        else:
            self.restart = self.restart_images[0]