import pygame

from core.generator.materials.imaterials import IMaterial
from core.generator.terrain.terrain import LevelDesigner


class IPlayer(IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/player/player_texture$0.png")
        self.id = -1
        self.can_spawn = True
        self.is_in_jump = False

    def spawn(self, screen, position, size):
        if not self.can_spawn:
            return
        self.pop_gen(pos=position, size=size)
        self.pop(screen)

    def can_spawn(self):
        return self.can_spawn

    def jump(self, power):
        print('jump')