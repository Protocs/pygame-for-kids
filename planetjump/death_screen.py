import pygame

from planetjump.utils import load_image, handle_close
from planetjump.score import Score, BestScore


class DeathScreen:
    def __init__(self, surface, score_group, score_counter):
        self.surface = surface
        self.score_counter = score_counter
        self.score_group = score_group
        self.best_score = BestScore(self.score_group)
        self.best_score.rect.x = self.score_counter.rect.x
        self.background = load_image("start_background.png")
        self.death = True
        self.you_died = load_image("you_died.png")

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
            handle_close(event)

    def update(self):
        self.mouse_handler()
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.you_died, (0, 50))
        self.surface.blit(self.restart[0], self.restart[1])
        self.score_group.draw(self.surface)
        self.score_counter.update()
        self.best_score.update()
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
