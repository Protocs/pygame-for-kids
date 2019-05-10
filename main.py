import pygame

from pygameforkids.other import SIZE
from pygameforkids.start_screen import StartScreen
from pygameforkids.game import Game

pygame.init()
screen = pygame.display.set_mode(SIZE)

while True:
    start = StartScreen(screen)
    start.run()
    game = Game(screen)
    game.run()

