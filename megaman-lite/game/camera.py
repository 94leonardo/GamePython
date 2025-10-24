# game/camera.py
from game.settings import WIDTH, HEIGHT


class Camera:
    def __init__(self, level_width, level_height):
        self.camera = {"x": 0, "y": 0}
        self.width = level_width
        self.height = level_height

    def apply_rect(self, rect):
        return rect.move(-self.camera["x"], -self.camera["y"])

    def update(self, target):
        # centrar en target, con límites
        x = target.rect.centerx - WIDTH // 2
        y = target.rect.centery - HEIGHT // 2

        x = max(0, min(x, self.width - WIDTH))
        y = max(0, min(y, self.height - HEIGHT))

        self.camera["x"] = int(x)
        self.camera["y"] = int(y)
