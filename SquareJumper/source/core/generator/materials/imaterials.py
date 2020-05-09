"""
IMaterial class is the class of allowed to create new material (terrain_block, spike, ...).
"""
import pygame


texture_list = {}


# Add texture in the map
def add_path(texture, path):
    texture_list[path] = texture


# Check if the map contain one texture by a texture path
def contain(path):
    return texture_list.__contains__(path)


# Obtain texture by her path
def get(path):
    return texture_list[path]


# Material Superclass
class IMaterial(pygame.sprite.Sprite):

    def __init__(self, texture_path="assets/textures/default/default.png", color=None):
        super().__init__()
        self.texture = None
        self.color = color
        if not contain(texture_path):
            self.texture = pygame.image.load(texture_path).convert_alpha()
            if self.color is not None:
                self.texture.fill((self.color[0], self.color[1], self.color[2]), special_flags=pygame.BLEND_MULT)
            add_path(self.texture, texture_path)
        else:
            self.texture = get(texture_path)
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

    # Modify the position of the material
    def set_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.location = Location(self.rect, self)
        self.teleport(location=self.location)

    # Generate position of the material
    def pop_gen(self, pos, size):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.base_rect[0] = pos[0]
        self.base_rect[1] = pos[1]
        self.size = size

    # Display the material
    def pop(self, screen):
        screen.blit(self.texture, self.rect)

    # Move the material
    def move(self, add, player, screen, windows_size, level):
        self.rect.x += add[0]

    # Modify the position of the material with Location class
    def teleport(self, location):
        self.rect.x = location.get_AA()[0]
        self.rect.y = location.get_AA()[1]

    # Set transparency value of the material
    def set_transparency(self, value=0.0):
        self.transparency = value

    # Set material full transparent
    def set_full_transparency(self):
        self.transparency = 1.0

    # Obtain the transparency
    def get_transparency(self):
        return self.transparency

    # Return True if full transparent
    def is_full_transparent(self):
        return self.transparency >= 1.0

    # Obtain material raw id
    def get_id(self):
        return self.id

    # Obtain dimension
    def get_box_dimension(self):
        return self.dimension

    # Obtain the position of the material
    def get_position(self):
        return self.rect

    # Obtain x position
    def get_position_x(self):
        return self.rect.x

    # Obtain y position
    def get_position_y(self):
        return self.rect.y

    # Obtain x dimension
    def get_dimension_x(self):
        return self.dimension[0]

    # Obtain y dimension
    def get_dimension_y(self):
        return self.dimension[1]

    # Get BoundingBox
    def get_bounding_box(self):
        return self.bounding_box

    # Get Location
    def get_location(self):
        return self.location


# BoundingBox class is used for manage IMaterial box
class BoundingBox:

    def __init__(self, material):
        self.material = material
        self.bounding_box = [
            [0, 0],
            [self.material.get_dimension_x(), 0],
            [self.material.get_dimension_x(), self.material.get_dimension_y()],
            [0, self.material.get_dimension_y()]
        ]
        self._id = [
            "aa",
            "ab",
            "bb",
            "ba"
        ]

    # Get all coin position
    def get_bounding_box(self):
        return self.bounding_box

    # Obtain coin position by id
    def get_coin_by_id(self, _id):
        if not self._id.__contains__(_id):
            return None
        return self.get_bounding_box()[self._id.index(_id)]

    # AA coin
    def get_AA_coin(self):
        return self.get_bounding_box()[0]

    # AB coin
    def get_AB_coin(self):
        return self.get_bounding_box()[1]

    # BB coin
    def get_BB_coin(self):
        return self.get_bounding_box()[2]

    # BA coin
    def get_BA_coin(self):
        return self.get_bounding_box()[3]

    def get_coins_position(self):
        return self.bounding_box


# Collision class is used for manage material collision (with player)
class Collision:

    def __init__(self, material):
        self.assignable = not material.is_full_transparent()
        self.bounding_box = material.get_bounding_box()
        self.location = material.get_location()
        self.material = material

    # Return the value of interaction between a material and a player
    def is_in_collision(self, player, screen, windows_size, level):
        _bounding_box = player.get_bounding_box()
        _location = player.get_location()
        aa = _location.get_AA()[0] > self.location.get_AA()[0] and _location.get_AA()[1] < self.location.get_AA()[1]
        ab = _location.get_AB()[0] < self.location.get_AB()[0] and _location.get_AB()[1] < self.location.get_AB()[1]
        bb = _location.get_BB()[0] < self.location.get_BB()[0] and _location.get_BB()[1] > self.location.get_BB()[1]
        ba = _location.get_BA()[0] + 50 > self.location.get_BA()[0] and _location.get_BA()[1] + 50 > self.location.get_BA()[1]
        bb_0 = _location.get_BB()[0] < self.location.get_BB()[0] and _location.get_BB()[1] + 50 > self.location.get_BB()[1]

        void_block = level.get_first_void_block_at(x=_location.get_block_location()[0])
        void_block_1 = level.get_first_void_block_at(x=_location.get_block_location()[0] + 1)

        block_location = get_block_location(_location.get()[0] + 26, _location.get()[1])

        if level.get_block_id_at(x=block_location[0] + 1, y=block_location[1] + 14) == 6 and not player.is_in_jump:
            return 5

        if level.get_block_id_at(x=block_location[0] + 1, y=block_location[1] + 14) == 2 and not player.is_in_jump:
            return 4

        if not player.is_in_jump and not player.is_auto_down and ba and bb_0 and _location.get()[1] == self.location.get()[1]:
            return 3

        if (_location.get_block_location()[1] - 1 > void_block[1] + 1 and
                _location.get_block_location()[1] - 1 > void_block_1[1] + 1) and not player.is_in_jump:
            return 2

        if (not bb and self.material.get_position_y() % 25 != 0) or not bb and not ab:
            return 0


# Block location is the custom location in the level grid
# This method is used for obtain this location by the frame location
def get_block_location(x=0, y=0):
    return int(x / 50), 13 - int((y + 26) / 50)


# Location class is used to manage IMaterial location
class Location:

    def __init__(self, rect, material):
        self._rect = rect
        self.material = material
        self.bounding_box = self.material.get_bounding_box()

    # Obtain AA coin location
    def get(self):
        return self.material.get_position_x(), self.material.get_position_y()

    # Obtain AA coin location
    def get_AA(self):
        return self.get()

    # Obtain AB coin location
    def get_AB(self):
        return self.material.get_position_x(), self.material.get_position_y() + self.bounding_box.get_AB_coin()[1]

    # Obtain BB coin location
    def get_BB(self):
        return self.material.get_position_x() + self.bounding_box.get_BB_coin()[0], self.material.get_position_y() + \
               self.bounding_box.get_BB_coin()[1]

    # Obtain BA coin location
    def get_BA(self):
        return self.material.get_position_x() + self.bounding_box.get_BA_coin()[0], self.material.get_position_y()

    # Move x location
    def add_x(self, x=0):
        self._rect.x += x

    # Move y location
    def add_y(self, y=0):
        self._rect.y += y

    # Move x and y location
    def add(self, x=0, y=0):
        self._rect.x += x
        self._rect.y += y

    # Obtain block location of this location
    def get_block_location(self):
        return int(self.get()[0] / 50), 13 - int((self.get()[1] + 26) / 50)
