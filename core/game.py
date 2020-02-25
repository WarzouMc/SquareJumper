from encodings.punycode import selective_find

from core.generator.terrain import Terrain


class Game:
    def __init__(self):
        self.key = {}
        self.terrain_block = {}

    def generation(self, screen, windows_size):
        for i in range(int(windows_size[0] / 25) * 2 + 1 + 3):
            for j in range(3):
                terrain = Terrain()
                terrain.pop_gen(pos=[i * 25 - 0, (windows_size[1] - 25) - j * 25], size=windows_size)
                terrain.pop(screen=screen)
                self.terrain_block[terrain] = "test"
