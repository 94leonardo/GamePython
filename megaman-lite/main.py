import pygame
import sys
from game.menu import main_menu
from game.engine import run_game


def main():
    pygame.init()

    # 🖥️ Obtener tamaño real del monitor
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    
    # 🔥 Ajusta el tamaño de la ventana dinámicamente
    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Megaman Lite (Pantalla Completa)")

    print(f"📏 Resolución del monitor detectada: {WIDTH}x{HEIGHT}")

    # 🕹️ Menú y juego
    try:
        main_menu(screen)
        run_game(screen)
    except pygame.error as e:
        print(f"Juego terminado: {e}")
    finally:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
