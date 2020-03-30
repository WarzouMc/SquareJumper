import math

from core.generator.materials.imaterials import IMaterial
from core.generator.materials.imaterials import Collision


def jump_equation(x, power):
    return int((power * (0.5 * math.pow(x, 2) - (4.0 * x) + 8) + 1) * 100) / 100


class IPlayer(IMaterial):

    def __init__(self):
        super().__init__(texture_path="assets/textures/player/player_texture$0.png")
        self.id = -1
        self.can_spawn = True
        self.is_in_jump = False
        self.jump_x = -0.1
        self.power = 0.0
        self.last_y = 0.0
        self.is_auto_down = False
        self.down_x = 3.9

    def spawn(self, screen, position, size):
        if not self.can_spawn:
            return
        self.pop_gen(pos=position, size=size)
        self.pop(screen)

    def can_spawn(self):
        return self.can_spawn

    def collision(self, level, block, windows_size, screen):
        for material in block:
            collision = Collision(material=material).is_in_collision(player=self, screen=screen,
                                                                     windows_size=windows_size,
                                                                     level=level)
            if collision == 1:
                self.stop_jump()
                self.stop_down()
            if collision == 2:
                self.auto_down()

    def jump(self, power, last_y):
        if not self.is_in_jump:
            self.is_in_jump = True
            self.jump_x = -0.1
            self.power = power
            self.last_y = last_y

    def jumping(self, screen):
        self.jump_x += 0.1
        temp = int(self.jump_x * 10) / 10
        position = self.get_position()
        if temp <= 4.0:
            position[1] -= int(jump_equation(x=temp, power=self.power))
        else:
            position[1] += int(jump_equation(x=temp, power=self.power))
        self.set_position(position=position)
        self.pop(screen=screen)
        if temp >= 8.0:
            self.jump_x = 0.0
            self.power = 0.0
            self.is_in_jump = False
            position[1] = self.last_y
            self.set_position(position=position)
            self.last_y = 0.0

    def stop_jump(self):
        self.jump_x = -0.1
        self.power = 0.0
        self.is_in_jump = False
        self.last_y = 0.0

    def auto_down(self):
        if not self.is_auto_down:
            self.is_auto_down = True
            self.down_x = 3.9

    def stop_down(self):
        self.down_x = 3.9
        self.is_auto_down = False

    def down(self, screen):
        self.down_x += 0.1
        temp = int(self.down_x * 10) / 10
        position = self.get_position()
        position[1] += int(jump_equation(x=temp, power=4))
        self.set_position(position=position)
        self.pop(screen=screen)
