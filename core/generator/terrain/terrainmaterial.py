import core.generator.materials.imaterials


class Void(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__()
        self.id = 0
        self.set_full_transparency()


class TerrainBlock(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/materials/terrain/terrain_block.png")
        self.id = 1


class Spike(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__()
        self.id = 2
