from core.generator.terrain import terrain

from core.player.iplayer import IPlayer


class Game:
    def __init__(self):
        self.key = {}
        self.terrain_block = {}
        self.player = IPlayer()
        self.level = terrain.get_levels()[0]
        self.background_movement = 0
        self.modulo_background_movement = 5

    def generation(self, screen, windows_size):
        level = terrain.get_levels()[0]
        for y in range(level.get_length()):
            for x in range(len(level.get_level_path()[y])):
                material = level.get_block_at(x=x, y=y)
                if x == 4 and y == 1:
                    self.player.spawn(screen=screen, position=[x * material.get_box_dimension()[0],
                                                               (windows_size[1] - material.get_box_dimension()[1]) - y
                                                               * material.get_box_dimension()[1]], size=windows_size)
                if material.get_id() != 0 and material.get_id() != 3:
                    material.pop_gen(pos=[x * material.get_box_dimension()[0],
                                          (windows_size[1] - material.get_box_dimension()[1]) - y *
                                          material.get_box_dimension()[1]], size=windows_size)
                    material.pop(screen=screen)
                self.terrain_block[material] = "add"

    def auto_move(self, screen, size):
        self.background_movement += 1
        self.level.get_background().pop(screen=screen)
        if self.background_movement % self.modulo_background_movement == 0:
            self.level.get_background().move(add=[-1, 0])
        useless_terrain = {}
        around_player = []
        player_block_location = self.player.get_location().get_block_location()
        for terrain_blocks in self.terrain_block:
            if terrain_blocks.get_position_x() >= -terrain_blocks.get_box_dimension()[0]:
                terrain_blocks.move(add=[-1, 0], player=self.player, screen=screen, windows_size=size, level=self.level)
                if terrain_blocks.get_position_x() <= size[0] + terrain_blocks.get_box_dimension()[0]:
                    if not (terrain_blocks.get_id() == 0 or terrain_blocks.get_id() == 3):
                        terrain_blocks.pop(screen=screen)
                    location = terrain_blocks.get_location().get_block_location()
                    if player_block_location[0] - 3 < location[0] < player_block_location[0] + 3 and \
                            player_block_location[1] - 3 < location[1] < player_block_location[1] + 3:
                        around_player.append(terrain_blocks)
            else:
                useless_terrain[terrain_blocks] = "remove"
        if len(useless_terrain) > 0:
            level_path = self.level.get_level_path()
            for y in range(len(level_path)):
                del level_path[y][0]
            self.level.set_path(path=level_path)

        self.player.collision(level=self.level, block=around_player, windows_size=size, screen=screen,
                              background=self.level.get_background())

        self.player.pop(screen=screen)
        for terrain_blocks in useless_terrain:
            self.terrain_block.__delitem__(terrain_blocks)

        if self.player.is_in_jump:
            self.player.jumping(level=self.level, screen=screen, background=self.level.get_background())

        if self.player.is_auto_down:
            self.player.down(level=self.level, screen=screen, background=self.level.get_background())
