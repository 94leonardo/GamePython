# main.py
import pygame
from game.menu import main_menu
from game.settings import WIDTH, HEIGHT

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Megaman Lite")
    main_menu(screen)
