import pygame
from game.settings import WIDTH, HEIGHT, FPS
from game.player import Player
from game.camera import Camera
from game.level_manager import LevelManager


def run_game(screen):
    """Bucle principal del juego"""
    print("🧩 Iniciando juego...")
    clock = pygame.time.Clock()
    running = True

    # 🔹 Crear LevelManager (ya carga el primer nivel)
    level_manager = LevelManager(screen)
    level = level_manager.current_level
    print(f"✅ Nivel cargado correctamente. Ancho: {level.width}, Alto: {level.height}")

    # 🔹 Crear jugador y cámara
    player = Player(64, HEIGHT - 200)
    camera = Camera(level.width, level.height)
    font = pygame.font.SysFont("Arial", 22)
    win = False

    # 🔁 Bucle principal
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # --- Lógica ---
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.update(1 / FPS, level)
        camera.update(player)

        # --- Colisión con meta ---
        for m in level.meta_rects:
            if player.rect.colliderect(m):
                print("🎯 ¡Nivel completado!")
                next_level = level_manager.load_next_level()
                if next_level:
                    level = next_level
                    camera = Camera(level.width, level.height)
                    player.rect.x, player.rect.y = 64, HEIGHT - 200
                    win = False
                    print(f"➡️ Cargado nivel {level_manager.current_level_number}")
                else:
                    print("🏁 ¡Has ganado el juego completo!")
                    win = True

        # --- Render ---
        screen.fill((30, 30, 40))
        level.draw(screen, camera)
        screen.blit(
            player.image,
            (
                player.rect.x - camera.camera.x,
                player.rect.y - camera.camera.y,
            ),
        )

        # HUD
        msg = (
            "🏆 ¡Juego completado! Presiona ESC para salir."
            if win
            else f"Llega a la casilla amarilla (Nivel {level_manager.current_level_number})"
        )
        surf = font.render(msg, True, (255, 255, 255))
        screen.blit(surf, (20, 20))

        pygame.display.flip()
        clock.tick(FPS)
