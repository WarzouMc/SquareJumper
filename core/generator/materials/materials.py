from core.generator.terrain import terrainmaterial


class Materials:

    def __init__(self):
        self.void = 0
        self.terrain_block = 1
        self.spike = 2

        self.by_id = [
            terrainmaterial.Void(),
            terrainmaterial.TerrainBlock(),
            terrainmaterial.Spike()
        ]

    def get_material_by_id(self, _id=0):
        return self.by_id[_id]
