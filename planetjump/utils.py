import pygame
import pickle

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


def save_progress(progress):
    try:
        with open("best_progress.txt", "wb") as f:
            pickle.dump(progress, f, pickle.HIGHEST_PROTOCOL)
    except OSError:
        pass


def load_best_progress():
    try:
        with open("best_progress.txt", "rb") as f:
            return pickle.load(f)
    except OSError:
        pass
    except pickle.PickleError:
        pass


SIZE = WIDTH, HEIGHT = 400, 800
