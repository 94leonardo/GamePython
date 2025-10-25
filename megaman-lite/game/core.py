# game/core.py
import pygame
from settings import *
from game.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        # Crear jugador
        self.player = Player(WIDTH // 2, HEIGHT - 40)
        self.all_sprites = pygame.sprite.Group(self.player)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.all_sprites.update(keys)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        # Suelo
        pygame.draw.rect(self.screen, GROUND_COLOR, (0, HEIGHT - 40, WIDTH, 40))
        # Sprites
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
