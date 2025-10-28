# game/menu.py
import pygame
import sys
from game.settings import WIDTH, HEIGHT, FPS
from game.engine import run_game


class Button:
    def __init__(self, text, pos, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
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

    # Botones
    button_play = Button(
        "JUGAR", (WIDTH // 2 - 100, HEIGHT // 2 - 40), 200, 50, start_game
    )
    button_quit = Button(
        "SALIR", (WIDTH // 2 - 100, HEIGHT // 2 + 30), 200, 50, quit_game
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

        # Renderizar título
        title_surf = title_font.render("MEGALITE", True, title_color)
        title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
        screen.blit(title_surf, title_rect)

        # Dibujar botones
        for b in buttons:
            b.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
