"""
This module allowed to create player
"""
import math
import pygame
import random

from core.generator.materials.imaterials import IMaterial
from core.generator.materials.imaterials import Collision


# This function give y position for a power and a distance from jump start
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

        self.jump_core = None

    # Spawn the player
    def spawn(self, screen, position, size):
        if not self.can_spawn:
            return
        self.jump_core = JumpCore(screen, size)
        self.pop_gen(pos=position, size=size)
        self.pop(screen)

    # Return true if the player can spawn
    def can_spawn(self):
        return self.can_spawn

    # Do action for a collision value
    def collision(self, level, block, windows_size, screen, game):
        self.jump_core.show(game)
        windows_y_modulo = windows_size[1] % 50
        if not self.is_in_jump and not self.is_auto_down and (windows_y_modulo - self.get_position_y()) % 50 != 0:
            position = self.get_position()
            position[1] -= position[1] % 50
            position[1] += windows_y_modulo
            self.set_position(position)

        for material in block:
            collision = Collision(material=material).is_in_collision(player=self, screen=screen,
                                                                     windows_size=windows_size,
                                                                     level=level)
            if collision == 1:
                self.stop_jump()
                self.stop_down()
                return
            if collision == 2:
                self.auto_down()
                return
            if collision == 3 or collision == 4:
                self.kill_(game, collision)
                return
            if collision == 5:
                self.win_(game)

    # Kill
    @staticmethod
    def kill_(game, cause):
        game.reset(cause)

    # Win
    @staticmethod
    def win_(game):
        game.win_()

    # Start a jump
    def jump(self, power, last_y):
        if not self.is_in_jump:
            self.is_in_jump = True
            self.jump_x = -0.1
            self.power = power
            self.last_y = last_y
            sound_index = random.randint(0, 6)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/player/jump_sound/jump$' + str(sound_index) + '.wav'))

    # Jump loop
    def jumping(self, game, level, screen):
        self.jump_x += 0.1
        temp = int(self.jump_x * 10) / 10
        position = self.get_position()
        if temp <= 4.0:
            position[1] -= int(jump_equation(x=temp, power=self.power))
        else:
            position[1] += int(jump_equation(x=temp, power=self.power))
        block_position = self.get_location().get_block_location()
        id = level.get_block_id_at(block_position[0], block_position[1] - 1)
        id_1 = level.get_block_id_at(block_position[0] + 1, block_position[1] - 1)
        id_2 = level.get_block_id_at(block_position[0], block_position[1])
        id_3 = level.get_block_id_at(block_position[0] + 1, block_position[1])
        self.set_position(position=position)
        self.pop(screen=screen)
        if (id_2 != 0 and id_2 != 3) and (id_3 != 0 and id_3 != 3):
            self.kill_(game, 6)
        if id == 3 or id_1 == 3:
            self.stop_jump()
            return

    # Stop the jump
    def stop_jump(self):
        self.jump_x = -0.1
        self.power = 0.0
        self.is_in_jump = False
        self.last_y = 0.0

    # Start auto down
    def auto_down(self):
        if not self.is_auto_down:
            self.is_auto_down = True
            self.down_x = 3.9

    # Stop auto down
    def stop_down(self):
        self.down_x = 3.9
        self.is_auto_down = False

    # Auto down loop
    def down(self, level, screen):
        self.down_x += 0.1
        temp = int(self.down_x * 10) / 10
        position = self.get_position()
        position[1] += int(jump_equation(x=temp, power=1))
        self.set_position(position=position)
        self.pop(screen=screen)
        block_position = self.get_location().get_block_location()
        id = level.get_block_id_at(block_position[0], block_position[1] - 1)
        id_1 = level.get_block_id_at(block_position[0] + 1, block_position[1] - 1)
        if id == 3 or id_1 == 3:
            self.stop_down()
            return

    # Obtain JumpCore
    def get_jump_core(self):
        return self.jump_core


# This class is used for manage player jump and graphic jump
class JumpCore(pygame.sprite.Sprite):

    def __init__(self, screen, window_size):
        super().__init__()
        self.screen = screen
        self.window_size = window_size
        self.bar_image = pygame.image.load("assets/textures/ig/jump/jump_load_bar/jump_bar$0.png").convert_alpha()
        self.bar_rect = self.bar_image.get_rect()
        self.bar_rect.x = self.window_size[0] / 2 - 200
        self.bar_rect.y = 20

        self.progression_image = pygame.image.load("assets/textures/ig/jump/jump_load_bar/jump_bar_progression$0.png") \
            .convert_alpha()
        self.progression_rect = self.progression_image.get_rect()
        self.progression_rect.x = self.window_size[0] / 2 - 199
        self.progression_rect.y = 21

        self.is_charged = False
        self.x = 0
        self.incrementation = 2

    # Manage jump bar
    def show(self, game):
        if game.key.get(pygame.K_SPACE):
            self.incrementation = 2
            if self.x < 399:
                self.x += 10
            self.is_charged = True
        elif self.x > 0:
            self.incrementation -= 1
            self.is_charged = self.incrementation > 0
            self.x -= 10
        self.screen.blit(self.bar_image, self.bar_rect)
        self.screen.blit(self.progression_image, self.progression_rect, (0, 0, self.x, 100))

    # Obtain current jump power
    def get_jump_power(self):
        if self.x > 275:
            return 0.5 + (((275 - (self.x - 275)) / 275) * 1.2)
        return 0.5 + (self.x / 275) * 1.2

    # Return True if the player can jump
    def is_charged_(self):
        return self.is_charged
