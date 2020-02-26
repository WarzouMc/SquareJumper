from encodings.punycode import selective_find

from core.generator.terrain import Terrain
from core.player.player import Player


class Game:
    def __init__(self):
        self.key = {}
        self.terrain_block = {}
        self.player = Player()

    def generation(self, screen, windows_size):
        for i in range(int(windows_size[0] / 25) * 2 + 1 + 3):
            for j in range(3):
                if 5 == i:
                    self.player.spawn(screen=screen, position=[i * 25, (windows_size[1] - 25) - 3 * 25])
                    self.player.pop(screen=screen)
                terrain = Terrain()
                terrain.pop_gen(pos=[i * 25, (windows_size[1] - 25) - j * 25], size=windows_size)
                terrain.pop(screen=screen)
                self.terrain_block[terrain] = "test"

    def auto_move(self, screen):
        for terrain in self.terrain_block:
            terrain.move(screen=screen, add=[-1, 0])
            terrain.pop(screen=screen)

    def player_jump(self):
        self.player.add_y()

    def player_management(self, screen):
        if self.player.rect.y != self.player.base_pos[1]:
            self.player.jump()
        else:
            self.player.reset_jump()
        self.player.pop(screen=screen)