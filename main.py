import pygame
from pygameforkids.other import SIZE
from pygameforkids.start_screen import StartScreen

pygame.init()
screen = pygame.display.set_mode(SIZE)

while True:
    start = StartScreen(screen)
    start.run()
