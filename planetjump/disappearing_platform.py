import pygame

from .other import load_image
from .platform import Platform


class DisappearingPlatform(Platform):
    def __init__(self, game, surface, y):
        super().__init__(game, surface, y)
        self.image = load_image("disappearing_platform.png")
