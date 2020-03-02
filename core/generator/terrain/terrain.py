from core.generator.materials import materials


def get_levels():
    level_list = [
        LevelDesigner(level=[
            [0]*100,
            [0]*100,
            [0]*100,
            [0]*100,
            [0]*12 + [1]*3 + [0]*85,
            [0]*10 + [1]*8 + [0]*82,
            [1]*40 + [0]*20 + [1]*40,
            [1]*50 + [0]*5 + [1]*45,
            [1]*100
        ])
    ]
    return level_list


class LevelDesigner:

    def __init__(self, level):
        self.level_path = level

    def get_length(self):
        return len(self.level_path)

    def get_level_path(self):
        return self.level_path

    def get_block_id_at(self, x=0, y=0):
        return self.level_path[(self.get_length() - y) - 1][x]

    def get_block_at(self, x=0, y=0):
        _id = self.get_block_id_at(x, y)
        return materials.Materials().get_material_by_id(_id=_id)
