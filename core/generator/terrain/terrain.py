from core.generator.materials import materials
from core.generator.terrain import terrainmaterial
from core.generator.materials.imaterials import Location


def get_levels():
    level_list = [
        LevelDesigner(level=[
            [0]*100,
            [0]*100,
            [0]*100,
            [0]*13 + [1]*2 + [0]*85,
            [0]*11 + [1]*5 + [0]*83,
            [0]*10 + [1]*9 + [0]*81,
            [1]*40 + [0]*20 + [1]*40,
            [1]*50 + [0]*5 + [1]*45,
            [1]*100
        ])
    ]
    return level_list


class LevelDesigner:

    def __init__(self, level):
        self.level_path = level

    def set_path(self, path):
        self.level_path = path

    def get_length(self):
        return len(self.level_path)

    def get_level_path(self):
        return self.level_path

    def get_block_id_at(self, x=0, y=0):
        if len(self.level_path[(self.get_length() - y) - 1]) <= x:
            return 0
        return self.level_path[(self.get_length() - y) - 1][x]

    def get_block_at(self, x=0, y=0):
        _id = self.get_block_id_at(x, y)
        material = materials.Materials().get_material_by_id(_id=_id)
        return material

    def get_first_void_block_at(self, x=0):
        for i in range(len(self.get_level_path())):
            if self.get_block_id_at(x=x, y=i) == 0:
                return x, i
        return None

    def get_first_void_block_nearby_to(self, x=0, around=0):
        for i in range(len(self.get_level_path())):
            if self.get_block_id_at(x=x + around, y=i) == 0:
                return x, i
        return None
