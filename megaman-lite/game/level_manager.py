from game.level import Level
import os


class LevelManager:
    def __init__(self, screen, game=None):
        self.screen = screen
        self.game = game
        self.current_level_number = 1
        self.max_levels = 3
        self.base_path = "game/levels"
        print(f"✅ LevelManager creado. Nivel actual: {self.current_level_number}")
        self.current_level = self.load_level(self.current_level_number)

    def load_level(self, number):
        path = os.path.join(self.base_path, f"level{number}.txt")
        print(f"🔍 Cargando nivel: {path}")
        try:
            return Level(number, self)
        except Exception as e:
            print(f"💥 Error al cargar el nivel {number}: {e}")
            raise


    def load_next_level(self):
        self.current_level_number += 1
        if self.current_level_number > self.max_levels:
            return None
        self.current_level = self.load_level(self.current_level_number)
        return self.current_level

    def update(self):
        self.current_level.update()

    def draw(self, screen):
        self.current_level.draw(screen)
