"""
IMaterial class is the class of allowed to create new material (terrain_block, spike, ...).
"""
import pygame


class IMaterial(pygame.sprite.Sprite):

    def __init__(self, texture_path="assets/textures/default/default.png"):
        super().__init__()
        self.texture = pygame.image.load(texture_path)
        self.rect = self.texture.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.base_rect = [0, 0]
        self.size = (0, 0)
        self.id = None
        self.dimension = self.texture.get_size()
        self.transparency = 0.0
        self.bounding_box = BoundingBox(bounding_box=[
            [0, 0],
            [self.get_x(), 0],
            [self.get_x(), self.get_y(),
            [0, self.get_y()]]
        ])
        self.bounding_box.get_coin_by_id(id="aa")
        self.location = Location(self.rect, self.bounding_box)

    # Material management
    def pop_gen(self, pos, size):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.base_rect[0] = pos[0]
        self.base_rect[1] = pos[1]
        self.size = size

    def pop(self, screen):
        screen.blit(self.texture, self.rect)

    def move(self, add):
        self.rect.x += add[0]

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

    def get_x(self):
        return self.get_position().x

    def get_y(self):
        return self.get_position().y

    def get_bounding_box(self):
        return self.bounding_box

    def get_location(self):
        return self.location


class BoundingBox:

    def __init__(self, bounding_box):
        self.bounding_box = bounding_box
        self._id = [
            "aa",
            "ab",
            "bb",
            "ba"
        ]

    def get_bounding_box(self):
        return self.bounding_box

    def get_coin_by_id(self, id):
        if not self._id.__contains__(id):
            return None
        print(str(self._id.index(id)))
        return self.get_bounding_box()[self._id.index(id)]

    def get_AA_coin(self):
        return self.get_bounding_box()[0]

    def get_AB_coin(self):
        return self.get_bounding_box()[1]

    def get_BB_coin(self):
        return self.get_bounding_box()[2]

    def get_BA_coin(self):
        return self.get_bounding_box()[3]

    def get_coin_position(self):
        return self.bounding_box


class Location:

    def __init__(self, rect, bounding_box):
        self._rect = rect
        self._bounding_box = bounding_box

    def get_aa_location(self, id):
        return self._rect.x, self._rect.y