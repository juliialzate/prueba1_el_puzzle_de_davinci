import pygame
from info import *
from Puzzle import puzzle

pygame.init()
puzzle = puzzle()
puzzle.run()
puzzle.pintar_imagenes()
pygame.display.update()

