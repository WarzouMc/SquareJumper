from core.generator.terrain import terrainmaterial


# List the different IMaterial
class Materials:

    def __init__(self):
        self.void = 0
        self.terrain_block = 1
        self.spike = 2
        self.bound_block = 3

        self.by_id = [
            terrainmaterial.Void(),
            terrainmaterial.TerrainBlock001(),
            terrainmaterial.Spike(),
            terrainmaterial.BoundBlock(),
            terrainmaterial.TerrainBlock002(),
            terrainmaterial.TerrainBlock003(),
            terrainmaterial.WinBlock()
        ]

    # Obtain material by id (not raw id -> data?)
    def get_material_by_id(self, _id=0):
        return self.by_id[_id]
