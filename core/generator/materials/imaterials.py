"""
IMaterial class is the class of allowed to create new material (terrain_block, spike, ...).
"""
import pygame

from core.generator.terrain import terrain


class IMaterial(pygame.sprite.Sprite):

    def __init__(self, texture_path="assets/textures/default/default.png"):
        super().__init__()
        self.texture = pygame.image.load(texture_path).convert_alpha()
        self.rect = self.texture.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.base_rect = [0, 0]
        self.size = (0, 0)
        self.id = None
        self.dimension = self.texture.get_size()
        self.transparency = 0.0
        self.bounding_box = BoundingBox(self)
        self.bounding_box.get_coin_by_id(_id="aa")
        self.location = Location(self.rect, self)

    def set_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.location = Location(self.rect, self)
        self.teleport(location=self.location)

    # Material management
    def pop_gen(self, pos, size):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.base_rect[0] = pos[0]
        self.base_rect[1] = pos[1]
        self.size = size

    def pop(self, screen):
        screen.blit(self.texture, self.rect)

    def move(self, add, player, screen, windows_size, level):
        self.rect.x += add[0]
        Collision(material=self).is_in_collision(_material=player, screen=screen, windows_size=windows_size, level=level)

    def teleport(self, location):
        self.rect.x = location.get_AA()[0]
        self.rect.y = location.get_AA()[1]

    # Material setters
    def set_transparency(self, value=0.0):
        self.transparency = value

    def set_full_transparency(self):
        self.transparency = 1.0

    # Material getters
    def get_transparency(self):
        return self.transparency

    def is_full_transparent(self):
        return self.transparency >= 1.0

    def get_id(self):
        return self.id

    def get_box_dimension(self):
        return self.dimension

    def get_position(self):
        return self.rect

    def get_position_x(self):
        return self.rect.x

    def get_position_y(self):
        return self.rect.y

    def get_x(self):
        return self.dimension[0]

    def get_y(self):
        return self.dimension[1]

    def get_bounding_box(self):
        return self.bounding_box

    def get_location(self):
        return self.location


class BoundingBox:

    def __init__(self, material):
        self.material = material
        self.bounding_box = [
            [0, 0],
            [self.material.get_x(), 0],
            [self.material.get_x(), self.material.get_y()],
            [0, self.material.get_y()]
        ]
        self._id = [
            "aa",
            "ab",
            "bb",
            "ba"
        ]

    def get_bounding_box(self):
        return self.bounding_box

    def get_coin_by_id(self, _id):
        if not self._id.__contains__(_id):
            return None
        return self.get_bounding_box()[self._id.index(_id)]

    def get_AA_coin(self):
        return self.get_bounding_box()[0]

    def get_AB_coin(self):
        return self.get_bounding_box()[1]

    def get_BB_coin(self):
        return self.get_bounding_box()[2]

    def get_BA_coin(self):
        return self.get_bounding_box()[3]

    def get_coins_position(self):
        return self.bounding_box


class Collision:

    def __init__(self, material):
        self.assignable = not material.is_full_transparent()
        self.bounding_box = material.get_bounding_box()
        self.location = material.get_location()
        self.material = material

    def is_in_collision(self, _material, screen, windows_size, level):
        _bounding_box = _material.get_bounding_box()
        _location = _material.get_location()
        aa = _location.get_AA()[0] > self.location.get_AA()[0] and _location.get_AA()[1] < self.location.get_AA()[1]
        ab = _location.get_AB()[0] < self.location.get_AB()[0] and _location.get_AB()[1] < self.location.get_AB()[1]
        bb = _location.get_BB()[0] < self.location.get_BB()[0] and _location.get_BB()[1] > self.location.get_BB()[1]
        ba = _location.get_BA()[0] > self.location.get_BA()[0] and _location.get_BA()[1] > self.location.get_BA()[1]
        if not (aa or ab or bb or ba) or not self.assignable:
            pos = level.get_first_void_block_at(x=_location.get_block_location()[0])
            first_void = level.get_block_at(x=pos[0], y=pos[1])
            first_void.pop_gen(pos=[pos[0] * first_void.get_box_dimension()[0],
                                  (windows_size[1] - first_void.get_box_dimension()[1]) - pos[1] *
                                  first_void.get_box_dimension()[1]], size=windows_size)
            _location = first_void.get_location()
            _material.set_position(position=[_location.get_AA()[0], _location.get_AA()[1]])
            _material.pop(screen=screen)


class Location:

    def __init__(self, rect, material):
        self._rect = rect
        self.material = material
        self.bounding_box = self.material.get_bounding_box()

    def get(self):
        return self.material.get_position_x(), self.material.get_position_y()

    def get_AA(self):
        return self.get()

    def get_AB(self):
        return self.material.get_position_x(), self.material.get_position_y() + self.bounding_box.get_AB_coin()[1]

    def get_BB(self):
        return self.material.get_position_x() + self.bounding_box.get_BB_coin()[0], self.material.get_position_y() + \
               self.bounding_box.get_BB_coin()[1]

    def get_BA(self):
        return self.material.get_position_x() + self.bounding_box.get_BA_coin()[0], self.material.get_position_y()

    def get_block_location(self):
        return int(self.get()[0] / 50), int(self.get()[1] / 50)
