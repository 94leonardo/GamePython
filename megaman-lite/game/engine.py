# game/engine.py
import pygame
from game.settings import WIDTH, HEIGHT, FPS
from game.player import Player
from game.level import Level
from game.camera import Camera


def run_game(screen):
    """Bucle principal del juego"""
    clock = pygame.time.Clock()
    running = True

    # Cargar nivel
    level_path = "game/levels/level1.txt"
    try:
        level = Level(level_path)
    except Exception as e:
        print(f"Error al cargar el nivel: {e}")
        return  # Evita que el juego crashee

    # Crear jugador y cámara
    player = Player(64, HEIGHT - 200)
    camera = Camera(level.width, level.height)
    font = pygame.font.SysFont("Arial", 22)
    win = False

    while running:
        # --- Entrada del usuario ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Lógica ---
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.update(1 / FPS, level)
        camera.update(player)

        # Detectar llegada a meta
        for m in level.meta_rects:
            if player.rect.colliderect(m):
                win = True

        # --- Renderizado ---
        screen.fill((30, 30, 40))
        level.draw(screen, camera)
        screen.blit(
            player.image,
            (
                player.rect.x - camera.camera["x"],
                player.rect.y - camera.camera["y"],
            ),
        )

        # HUD
        msg = (
            "¡Has llegado a la meta! Presiona ESC para salir."
            if win
            else "Llega a la casilla amarilla (M)"
        )
        surf = font.render(msg, True, (255, 255, 255))
        screen.blit(surf, (20, 20))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
