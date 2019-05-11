import pygame

from os import path


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter((self.x, self.y))


def load_image(filename):
    fullname = path.join("data", "images", filename)
    return pygame.image.load(fullname).convert_alpha()


def handle_close(event):
    if event.type == pygame.QUIT:
        terminate()


def terminate():
    pygame.quit()
    exit()


SIZE = WIDTH, HEIGHT = 400, 800
