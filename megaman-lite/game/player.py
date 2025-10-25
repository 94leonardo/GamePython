# game/player.py
import pygame
from game.settings import PLAYER_SPEED, PLAYER_RUN_MULT, PLAYER_JUMP_SPEED, GRAVITY


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # sprite provisional: rect simple
        self.image = pygame.Surface((32, 40), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (220, 60, 80), (0, 0, 32, 40))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.facing = 1

    def handle_input(self, keys):
        speed = PLAYER_SPEED
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = int(PLAYER_SPEED * PLAYER_RUN_MULT)
        self.vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -speed
            self.facing = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = speed
            self.facing = 1
        if (keys[pygame.K_z] or keys[pygame.K_SPACE]) and self.on_ground:
            self.vy = PLAYER_JUMP_SPEED
            self.on_ground = False

    def apply_gravity(self):
        self.vy += GRAVITY
        if self.vy > 20:
            self.vy = 20

    def update(self, dt, level):

        # movimiento horizontal con colisión tile-based
        self.rect.x += self.vx
        self._collide(self.vx, 0, level.tiles)

        # gravedad + colisión vertical
        self.apply_gravity()
        self.rect.y += int(self.vy)
        self.on_ground = False
        self._collide(0, self.vy, level.tiles)

    def _collide(self, vx, vy, tiles):
        for t in tiles:
            if self.rect.colliderect(t):
                if vx > 0:  # moviendo a la derecha
                    self.rect.right = t.left
                if vx < 0:  # izquierda
                    self.rect.left = t.right
                if vy > 0:  # cayendo
                    self.rect.bottom = t.top
                    self.vy = 0
                    self.on_ground = True
                if vy < 0:  # subiendo
                    self.rect.top = t.bottom
                    self.vy = 0
    
