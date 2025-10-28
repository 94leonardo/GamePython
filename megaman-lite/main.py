# main.py
import pygame
import sys
from game.menu import main_menu
from game.settings import WIDTH, HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Megaman Lite")

    try:
        main_menu(screen)
    except pygame.error as e:
        print(f"Juego terminado: {e}")
    finally:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
