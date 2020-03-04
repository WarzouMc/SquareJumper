import pygame

from core.generator.materials.imaterials import IMaterial
from core.generator.terrain.terrain import LevelDesigner


class IPlayer(IMaterial):

    def __init__(self):
        super().__init__()
        self.id = -1
        self.can_spawn = True
        self.is_in_jump = False
        self.location = None

    def spawn(self, position, size):
        if self.can_spawn:
            return
        self.location = self.get_bounding_box()
        self.pop_gen(pos=position, size=size)

    def can_spawn(self):
        return self.can_spawn

    def jump(self, power):
        print('jump')