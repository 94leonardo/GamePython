# game/engine.py
import pygame
from game.settings import WIDTH, HEIGHT, FPS
from game.player import Player
from game.level import Level
from game.camera import Camera


class Engine:
    def __init__(self, screen):
        pygame.display.set_caption("MegaLite - Stage Básico")
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        layout = [
            "100000000000000000000000000000000000000001",
            "100000000000000000000000000000000000000001",
            "100000000000000000000000000000000000000001",
            "100000000000000000000000000000000000000001",
            "100000000000000000000000000000000000000001",
            "100000110000000000000000000000000000000001",
            "100001111000000000000001111000000000000001",
            "100011111100000011111000000000000000000001",
            "10111111111110000000000000000000M000000001",
            "111111111111111111111111111111111111111111",
        ]

        self.level = Level(layout)
        self.player = Player(64, HEIGHT - 200)
        self.camera = Camera(self.level.width, self.level.height)
        self.font = pygame.font.SysFont("Arial", 20)
        self.win = False

    def handle_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.running = False
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                self.running = False

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        self.player.update(dt, self.level)
        self.camera.update(self.player)

        # Verificar si llegó al punto amarillo
        for m in self.level.meta_rects:
            if self.player.rect.colliderect(m):
                self.win = True

        if self.win:
            self.reset_level()

    def reset_level(self):
        """Reinicia el nivel"""
        self.player.rect.x = 64
        self.player.rect.y = HEIGHT - 200
        self.win = False

    def draw(self):
        self.screen.fill((30, 30, 40))
        self.level.draw(self.screen, self.camera)

        # Dibuja el jugador con desplazamiento de cámara
        draw_pos = (
            self.player.rect.x - self.camera.camera["x"],
            self.player.rect.y - self.camera.camera["y"],
        )
        self.screen.blit(self.player.image, draw_pos)

        text = (
            "¡GANASTE! Presiona ESC para salir o camina para reiniciar."
            if self.win
            else "Objetivo: llega al punto amarillo (M)."
        )
        surf = self.font.render(text, True, (230, 230, 230))
        self.screen.blit(surf, (10, 10))

        pygame.display.flip()


def run_game(screen):
    """Bucle principal del juego"""
    engine = Engine(screen)
    clock = pygame.time.Clock()

    while engine.running:
        engine.handle_events()
        engine.update(clock.get_time() / 1000)
        engine.draw()
        clock.tick(FPS)

    pygame.quit()
