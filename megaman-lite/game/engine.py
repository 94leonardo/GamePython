# game/engine.py
import pygame
from game.settings import WIDTH, HEIGHT, FPS
from game.player import Player
from game.level import Level
from game.camera import Camera


class Engine:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MegaLite - Stage Básico")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # Nivel: lista de strings (fila superior = 0)
        layout = [
            "000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000",
            "00000000000000000000000000000000M000000000",
            "000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000",
            "000000110000000000000000000000000000000000",
            "000001111000000000000000000000000000000000",
            "000011111100000000000000000000000000000000",
            "001111111111100000000000000000000000000000",
            "111111111111111111111111111111111111111111",
        ]
        self.level = Level(layout)
        self.player = Player(64, HEIGHT - 200)
        self.sprites = pygame.sprite.Group(self.player)
        self.camera = Camera(self.level.width, self.level.height)
        self.font = pygame.font.SysFont("Arial", 20)
        self.win = False

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)
            self._events()
            self._update(dt)
            self._draw()
        pygame.quit()

    def _events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.running = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.running = False

    def _update(self, dt):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        self.player.update(dt, self.level)
        self.camera.update(self.player)

        for m in self.level.meta_rects:
            if self.player.rect.colliderect(m):
                self.win = True

    def _draw(self):
        self.screen.fill((30, 30, 40))
        self.level.draw(self.screen, self.camera)

        # dibujar player con offset de cámara
        draw_pos = (
            self.player.rect.x - self.camera.camera["x"],
            self.player.rect.y - self.camera.camera["y"],
        )
        self.screen.blit(self.player.image, draw_pos)

        # HUD
        text = (
            "WIN! Presiona ESC para salir."
            if self.win
            else "Objetivo: llegar a la casilla amarilla (M)."
        )
        surf = self.font.render(text, True, (230, 230, 230))
        self.screen.blit(surf, (10, 10))

        pygame.display.flip()
