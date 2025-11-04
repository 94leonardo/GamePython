# game/menu.py
import pygame
import sys
from game.settings import WIDTH, HEIGHT, FPS
from game.engine import run_game


class Button:
    def __init__(self, text, pos, width, height, callback):
        self.text = text
        # Asegurar que el botón esté centrado horizontalmente
        x = pos[0] - width // 2
        self.rect = pygame.Rect(x, pos[1], width, height)
        self.color = (100, 100, 255)
        self.hover_color = (150, 150, 255)
        self.callback = callback
        self.font = pygame.font.SysFont("Arial", 28)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


def main_menu(screen):
    running = True
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 80)
    title_color = (255, 255, 255)
    title_glow = 0

    # Funciones locales
    def start_game():
        run_game(screen)

    def quit_game():
        pygame.quit()
        sys.exit()

    # 🔥 BOTONES CENTRADOS - Coordenadas corregidas
    button_width, button_height = 200, 50

    # Calcular posiciones Y centradas verticalmente
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    button_play = Button(
        "JUGAR",
        (center_x, center_y - 30),  # Centrado horizontal, ligeramente arriba del centro
        button_width,
        button_height,
        start_game,
    )
    button_quit = Button(
        "SALIR",
        (center_x, center_y + 40),  # Centrado horizontal, ligeramente abajo del centro
        button_width,
        button_height,
        quit_game,
    )

    buttons = [button_play, button_quit]

    # Bucle principal del menú
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for b in buttons:
                b.handle_event(event)

        # Fondo animado
        screen.fill((30, 30, 40))
        title_glow = (title_glow + 2) % 255
        title_color = (255, 255 - title_glow // 2, 255 - title_glow // 2)

        # 🔥 TÍTULO CENTRADO
        title_surf = title_font.render("MEGALITE", True, title_color)
        title_rect = title_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 4)
        )  # 1/4 desde arriba
        screen.blit(title_surf, title_rect)

        # 🔥 TEXTO INFORMATIVO CENTRADO (opcional)
        info_font = pygame.font.SysFont("Arial", 18)
        info_text = info_font.render(
            "Plataformas estilo Megaman", True, (200, 200, 200)
        )
        info_rect = info_text.get_rect(center=(WIDTH // 2, HEIGHT // 4 + 60))
        screen.blit(info_text, info_rect)

        # Dibujar botones (ya están centrados)
        for b in buttons:
            b.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
