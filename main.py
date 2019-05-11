import pygame

from planetjump.utils import SIZE
from planetjump.start_screen import StartScreen
from planetjump.game import Game

pygame.init()
screen = pygame.display.set_mode(SIZE)

while True:
    start = StartScreen(screen)
    start.run()
    game = Game(screen)
    game.run()
