from core.generator.terrain import terrain
from core.player.player import Player

from core.player.iplayer import IPlayer


class Game:
    def __init__(self):
        self.key = {}
        self.terrain_block = {}
        self.player = Player()

    def generation(self, screen, windows_size):
        level = terrain.get_levels()[0]
        for y in range(level.get_length()):
            for x in range(len(level.get_level_path()[y])):
                material = level.get_block_at(x=x, y=y)
                if x == 5 and y == 3:
                    self.player.spawn(screen=screen, position=[x * material.get_box_dimension()[0], (windows_size[1] - material.get_box_dimension()[1]) - 3 * material.get_box_dimension()[1]])
                    self.player.pop(screen=screen)
                if not material.is_full_transparent():
                    material.pop_gen(pos=[x * material.get_box_dimension()[0],
                                          (windows_size[1] - material.get_box_dimension()[1]) - y *
                                          material.get_box_dimension()[1]], size=windows_size)
                    material.pop(screen=screen)
                    self.terrain_block[material] = "add"

    def auto_move(self, screen, size):
        player = IPlayer().spawn(position=[0, 0], size=size)
        useless_terrain = {}
        t = terrain.materials.Materials().get_material_by_id(_id=2)
        t.pop_gen(pos=[400, (25 * 25) - 150], size=[25 * 50, 25 * 25])
        t.pop(screen=screen)
        for terrain_blocks in self.terrain_block:
            if terrain_blocks.get_x() >= -terrain_blocks.get_box_dimension()[0]:
                terrain_blocks.move(add=[-5, 0], player=t, screen=screen)
                if terrain_blocks.get_x() <= size[0] + terrain_blocks.get_box_dimension()[0]:
                    terrain_blocks.pop(screen=screen)
            else:
                useless_terrain[terrain_blocks] = "test"

        for terrain_blocks in useless_terrain:
            self.terrain_block.__delitem__(terrain_blocks)

    def player_jump(self):
        self.player.add_y()

    def player_management(self, screen):
        if self.player.rect.y != self.player.base_pos[1]:
            self.player.jump()
        else:
            self.player.reset_jump()
        self.player.pop(screen=screen)
