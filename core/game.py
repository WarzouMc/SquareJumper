from core.generator.terrain import Terrain


class Game:
    def __init__(self):
        self.key = {}

    def generation(self, screen, windows_size):
        terrain = Terrain()
        for i in range(int(windows_size[0] / 25) + 1):
            for j in range(3):
                terrain.pop(screen=screen, position=[i * terrain.box[0], (windows_size[1] - terrain.box[1]) - j * terrain.box[1]])
