# game/level.py
import pygame
import os
from game.settings import TILE_SIZE


class Level:
    """
    Clase que representa un nivel del juego cargado desde un archivo de texto.
    Cada carácter representa un bloque:
    '1' -> tile/ground
    '0' -> vacío
    'M' -> meta (llegada)
    """

    def __init__(self, level_number, manager):
        self.level_number = level_number
        self.manager = manager
        self.screen = manager.screen
        self.tiles = []
        self.meta_rects = []
        self.width = 0
        self.height = 0

        # Cargar archivo de nivel
        level_path = os.path.join("game", "levels", f"level{level_number}.txt")
        self.load_level(level_path)
        with open(level_path, "r") as f:
            self.map_data = [line.strip() for line in f.readlines() if line.strip()]

        # Calcular tamaño del tile dinámicamente
        screen_width, screen_height = self.screen.get_size()
        self.rows = len(self.map_data)
        self.cols = len(self.map_data[0])
        self.tile_width = screen_width // self.cols
        self.tile_height = screen_height // self.rows
        self.tile_size = min(self.tile_width, self.tile_height)  # cuadrado

        print(
            f"🧱 Tamaño del tile: {self.tile_size}px ({self.cols}x{self.rows} celdas)"
        )

    def load_level(self, file_path):
        """Carga el nivel desde un archivo de texto"""
        try:
            with open(file_path, "r") as f:
                layout = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"❌ Archivo de nivel no encontrado: {file_path}")
            return

        y = 0
        for row in layout:
            x = 0
            for col in row.strip():
                if col == "1":
                    rect = pygame.Rect(
                        x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    )
                    self.tiles.append(rect)
                elif col == "M":
                    rect = pygame.Rect(
                        x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE
                    )
                    self.meta_rects.append(rect)
                x += 1
            y += 1

        self.width = len(layout[0]) * TILE_SIZE
        self.height = len(layout) * TILE_SIZE
        print(
            f"✅ Nivel cargado correctamente: {file_path} ({self.width}x{self.height})"
        )

    def draw(self, screen, camera):
        """Dibuja los bloques y la meta"""
        for tile in self.tiles:
            pygame.draw.rect(
                screen,
                (100, 100, 100),
                (
                    tile.x - camera.camera.x,
                    tile.y - camera.camera.y,
                    TILE_SIZE,
                    TILE_SIZE,
                ),
            )
        for m in self.meta_rects:
            pygame.draw.rect(
                screen,
                (255, 255, 0),
                (
                    m.x - camera.camera.x,
                    m.y - camera.camera.y,
                    TILE_SIZE,
                    TILE_SIZE,
                ),
            )
