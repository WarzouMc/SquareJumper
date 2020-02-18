from encodings.punycode import selective_find

from core.generator.terrain import Terrain


class Game:
    def __init__(self):
        self.key = {}
        self.terrain_block = {}

    def generation(self, screen, windows_size):
        for i in range(int(windows_size[0] / 3750) + 1):
            for j in range(1):
                terrain = Terrain()
                terrain.pop(screen=screen, position=[i * terrain.box[0] - 1250, (windows_size[1] - terrain.box[1]) - j * terrain.box[1]])
                self.terrain_block[terrain] = "test"
