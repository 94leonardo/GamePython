import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(100, 100, 100)):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
