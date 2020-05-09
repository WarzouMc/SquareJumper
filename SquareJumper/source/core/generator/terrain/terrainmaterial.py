"""
This module is used to create different IMaterial
"""
import core.generator.materials.imaterials


class Void(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__()
        self.id = 0
        self.set_full_transparency()


class BoundBlock(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__()
        self.id = 3
        self.set_full_transparency()


class TerrainBlock001(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/materials/terrain/terrain_block$0.png", color=[100, 100, 255])
        self.id = 1


class TerrainBlock002(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/materials/terrain/terrain_block$1.png", color=[200, 50, 200])
        self.id = 1


class TerrainBlock003(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/materials/terrain/terrain_block$2.png", color=[255, 100, 0])
        self.id = 1


class Spike(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/materials/spike/spike$0.png", color=[255, 50, 100])
        self.id = 2


class WinBlock(core.generator.materials.imaterials.IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/materials/win/win_block$0.png", color=[255, 100, 100])
        self.id = 6
