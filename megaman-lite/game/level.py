# game/level.py
import pygame
from game.settings import TILE_SIZE


class Level:
    """
    Nivel simple construido desde lista de strings.
    '1' -> tile/ground
    '0' -> vacío
    'M' -> meta (llegada)
    """

    def __init__(self, layout):
        self.layout = layout
        self.width = len(layout[0]) * TILE_SIZE
        self.height = len(layout) * TILE_SIZE
        self.tiles = []
        self.meta_rects = []
        self._build()

    def _build(self):
        for row_idx, row in enumerate(self.layout):
            for col_idx, ch in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                if ch == "1":
                    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    self.tiles.append(rect)
                elif ch == "M":
                    self.meta_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

    def draw(self, surface, camera):
        # dibuja tiles simples (puedes reemplazarlos por sprites luego)
        for t in self.tiles:
            r = camera.apply_rect(t)
            pygame.draw.rect(surface, (70, 120, 200), r)
        for m in self.meta_rects:
            r = camera.apply_rect(m)
            pygame.draw.rect(surface, (220, 200, 70), r)
