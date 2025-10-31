# game/level.py
import pygame
from game.settings import TILE_SIZE


class Level:
    """
    Clase Level: representa un nivel 2D basado en un archivo o lista.
    '1' -> bloque sólido
    '0' -> vacío
    'M' -> meta (llegada)
    """

    def __init__(self, source):
        self.tiles = []  # Bloques sólidos
        self.meta_rects = []  # Zonas meta amarillas

        if isinstance(source, str):  # Si se pasa una ruta
            self._load_from_file(source)
        elif isinstance(source, list):  # Si se pasa layout directo
            self._load_from_layout(source)
        else:
            raise TypeError("El nivel debe ser un archivo o una lista de strings.")

    def _load_from_file(self, file_path):
        """Carga un nivel desde un archivo de texto"""
        with open(file_path, "r") as f:
            layout = [line.strip() for line in f.readlines()]
        self._load_from_layout(layout)

    def _load_from_layout(self, layout):
        """Carga un nivel desde una lista de strings"""
        self.layout = layout
        self.width = len(layout[0]) * TILE_SIZE
        self.height = len(layout) * TILE_SIZE

        for y, row in enumerate(layout):
            for x, cell in enumerate(row):
                if cell == "1":
                    rect = pygame.Rect(
                        x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    )
                    self.tiles.append(rect)
                elif cell == "M":
                    meta = pygame.Rect(
                        x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    )
                    self.meta_rects.append(meta)

    def draw(self, screen, camera):
        """Dibuja el nivel con desplazamiento de cámara"""
        for tile in self.tiles:
            pygame.draw.rect(
                screen,
                (100, 100, 100),
                (
                    tile.x - camera.camera["x"],
                    tile.y - camera.camera["y"],
                    TILE_SIZE,
                    TILE_SIZE,
                ),
            )
        for m in self.meta_rects:
            pygame.draw.rect(
                screen,
                (255, 255, 0),
                (
                    m.x - camera.camera["x"],
                    m.y - camera.camera["y"],
                    TILE_SIZE,
                    TILE_SIZE,
                ),
            )
