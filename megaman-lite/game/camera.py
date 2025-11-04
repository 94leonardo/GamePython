# game/camera.py
import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, rect):
        """Aplica el desplazamiento de la cámara a un rectángulo."""
        return rect.move(-self.camera_rect.topleft[0], -self.camera_rect.topleft[1])

    def update(self, target):
        """Centra la cámara en el objetivo (jugador), sin salirse del mapa."""
        x = -target.rect.x + 480  # mitad de pantalla (960/2)
        y = -target.rect.y + 270  # mitad de pantalla (540/2)

        # Limitar la cámara a los bordes del nivel
        x = min(0, x)
        x = max(-(self.width - 960), x)
        y = min(0, y)
        y = max(-(self.height - 540), y)

        self.camera_rect = pygame.Rect(x, y, self.width, self.height)
