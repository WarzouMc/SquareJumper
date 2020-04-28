from core.generator.materials import materials
from core.generator.background.background import Backgrounds


def get_levels():
    level_0 = [
        "#################################################################################"*3,
        "#################################################################################"*3,
        "#################################################################################"*3,
        "#################################################################################"*3,
        "#################################################################################"*3,
        "#################################################################################"*3,
        "#############***####*#########################################***###*############"*3,
        "##########***$$$****$*####***#############################****$$$***$*###########"*3,
        "#########*$$$$$$$$$$$$****$$$**#########################**$$$$$$$$$$$$*##########"*3,
        "########*$$$$$$$$$$$$$$$$$$$$$$######################***$$$$$$$$$$$$$$$***#######"*3,
        "######**$$$$$$$$$$$$$$$$$$$$$$$***********#######****$$$$$$$$$$$$$$$$$$$$$*******"*3,
        "******$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*******$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"*3,
        "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"*3
    ]
    value = {'#': 0, '$': 1, '*': 3}

    level_list = [
        LevelDesigner(level=to_level_path(value=value, string=level_0), background=Backgrounds().background_list[0])
    ]
    return level_list


def to_level_path(value, string):
    x_len = len(string[0])
    y_len = len(string)
    level = [[0]*x_len]*y_len
    y = 0
    for line in string:
        x = 0
        x_path = [0] * x_len
        for material in line:
            x_path[x] = int(value.get(material))
            x += 1
        level[y] = x_path
        y += 1
    return level


class LevelDesigner:

    def __init__(self, level, background):
        self.level_path = level
        self.background = background

    def set_path(self, path):
        self.level_path = path

    def get_length(self):
        return len(self.level_path)

    def get_level_path(self):
        return self.level_path

    def get_background(self):
        return self.background

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
            if self.get_block_id_at(x=x, y=i) == 0 or self.get_block_id_at(x=x, y=i) == 3:
                return x, i - 1
        return None

    def get_first_void_block_nearby_to(self, x=0, around=0):
        for i in range(len(self.get_level_path())):
            if self.get_block_id_at(x=x + around, y=i) == 0 or self.get_block_id_at(x=x + around, y=i) == 3:
                return x, i
        return None
