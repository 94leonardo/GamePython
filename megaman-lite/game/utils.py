# game/utils.py
import pygame
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def load_image(path):
    full = os.path.join(BASE_DIR, path)
    return pygame.image.load(full).convert_alpha()
