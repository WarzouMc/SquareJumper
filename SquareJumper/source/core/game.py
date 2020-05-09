import pygame

from core.generator.terrain import terrain
from core.player.iplayer import IPlayer
from core.screens.screens.menu_screen import Menu
from core.screens.screens.menu_screen import DeathMenu
from core.screens.screens.menu_screen import WinMenu


# This class manage the game
class Game:
    def __init__(self, screen, window_size):
        self.screen = screen
        self.window_size = window_size
        self.is_run = False
        self.current_level = -1
        self.level_runner = None
        self.key = {}

        self.pause = False

        self.current_screen = Menu()
        self.current_screen.show(self.screen)
        self.black = 0, 0, 0

    # Get the current screen
    def get_current_screen(self):
        return self.current_screen

    # Reset game
    def reset(self, cause):
        if self.level_runner is not None:
            point = self.level_runner.distance
            self.level_runner.end()
            self.current_screen = DeathMenu(point, cause)
            self.current_level = -1
            self.level_runner = None
            self.is_run = False

    # Win a game
    def win_(self):
        if self.level_runner is not None:
            point = self.level_runner.distance
            self.level_runner.end()
            self.current_screen = WinMenu(point, self.level_runner.current_level)
            self.current_level = -1
            self.level_runner = None
            self.is_run = False

    # Game loop
    def default_run(self):
        self.screen.fill(self.black)
        if self.get_level_runner() is None:
            self.current_screen.show(screen=self.screen)
            pygame.display.flip()
            return
        self.get_level_runner().auto_move()
        pygame.display.flip()

    # Start a game
    def run_game(self, level):
        self.current_screen = None
        self.is_run = True
        self.current_level = level
        self.level_runner = LevelRunner(self.current_level, self.screen, self.window_size, self)
        self.get_level_runner().generate()

    # Display menu
    def show_menu(self):
        self.current_screen = Menu()

    # Return true if game is running
    def is_running(self):
        return self.is_run

    # Obtain the current level
    def get_current_level(self):
        return self.level

    # Obtain LevelRunner
    def get_level_runner(self):
        return self.level_runner


# Load level
class LevelRunner:

    def __init__(self, current_level, screen, window_size, game):
        self.current_level = current_level
        self.screen = screen
        self.window_size = window_size
        self.game = game

        self.terrain_block = {}
        self.player = IPlayer()
        self.level = terrain.get_levels()[self.current_level]
        self.background_movement = 0
        self.modulo_background_movement = 5

        pygame.mixer.music.load("assets/sounds/play/level_0/Androidal.mp3")
        self.distance = 0

        self.bar_image = pygame.image.load("assets/textures/ig/progress_bar/background_bar$0.png").convert_alpha()
        self.bar_rect = self.bar_image.get_rect()
        self.bar_rect.centerx = window_size[0] / 2
        self.bar_rect.y = 295

        self.progression_image = pygame.image.load("assets/textures/ig/progress_bar/progress_bar$0.png") \
            .convert_alpha()
        self.progression_rect = self.progression_image.get_rect()
        self.progression_rect.centerx = window_size[0] / 2
        self.progression_rect.y = 296
        self.progression_dim = self.progression_image.get_size()

    # Generate the map
    def generate(self):
        level = terrain.get_levels()[self.current_level]
        for y in range(level.get_length()):
            for x in range(len(level.get_level_path()[y])):
                material = level.get_block_at(x=x, y=y)
                if x == 6 and y == 1:
                    self.player.spawn(screen=self.screen, position=[x * material.get_box_dimension()[0],
                                                                    (self.window_size[1] - material.get_box_dimension()
                                                                    [1]) - y * material.get_box_dimension()[1]],
                                      size=self.window_size)
                if material.get_id() != 0 and material.get_id() != 3:
                    material.pop_gen(pos=[x * material.get_box_dimension()[0],
                                          (self.window_size[1] - material.get_box_dimension()[1]) - y *
                                          material.get_box_dimension()[1]], size=self.window_size)
                self.terrain_block[material] = "add"
                if len(self.terrain_block) % 51 != 0:
                    continue
                charge = (int(1000 * (len(self.terrain_block) / level.get_blocks()) * 100)) / 1000
                charge_font = pygame.font.SysFont("Consolas", 30)
                charge_font_0 = pygame.font.SysFont("Consolas", 15)
                charge_texture = charge_font.render(str(charge) + "%", False, (255, 255, 255))
                charge_texture_0 = charge_font_0.render(str(len(self.terrain_block)) + "/" + str(level.get_blocks()),
                                                        False, (255, 255, 255))
                self.screen.fill((0, 0, 0))
                charge_rect = charge_texture.get_rect()
                charge_rect_0 = charge_texture_0.get_rect()
                charge_rect.center = (self.window_size[0] / 2, self.window_size[1] / 2)
                charge_rect_0.center = (self.window_size[0] / 2, (self.window_size[1] / 2) - 40)

                self.screen.blit(self.bar_image, self.bar_rect)
                self.screen.blit(self.progression_image, self.progression_rect, (0, 0, self.progression_dim[0]
                                                                                 * (charge / 100), 100))

                self.screen.blit(charge_texture, charge_rect)
                self.screen.blit(charge_texture_0, charge_rect_0)
                pygame.display.flip()
        pygame.mixer.music.play()
        pygame.mouse.set_visible(False)

    # Move the map
    def auto_move(self):
        self.background_movement += 1
        if self.background_movement % 100 == 0:
            self.distance += 1
        self.level.get_background().pop(screen=self.screen)
        if self.background_movement % self.modulo_background_movement == 0:
            self.level.get_background().move(add=[-1, 0])
        useless_terrain = {}
        around_player = []
        player_block_location = self.player.get_location().get_block_location()
        for terrain_blocks in self.terrain_block:
            if terrain_blocks.get_position_x() >= -terrain_blocks.get_box_dimension()[0]:
                terrain_blocks.move(add=[-3, 0], player=self.player, screen=self.screen, windows_size=self.window_size,
                                    level=self.level)
                if terrain_blocks.get_position_x() <= self.window_size[0] + terrain_blocks.get_box_dimension()[0]*-(self.distance / 25):
                    if not (terrain_blocks.get_id() == 0 or terrain_blocks.get_id() == 3):
                        terrain_blocks.pop(screen=self.screen)
                    location = terrain_blocks.get_location().get_block_location()
                    if player_block_location[0] - 3 < location[0] < player_block_location[0] + 3 and \
                            player_block_location[1] - 3 < location[1] < player_block_location[1] + 3:
                        around_player.append(terrain_blocks)
            else:
                useless_terrain[terrain_blocks] = "remove"
        if len(useless_terrain) > 0:
            level_path = self.level.get_level_path()
            for y in range(len(level_path)):
                del level_path[y][0]
            self.level.set_path(path=level_path)

        self.player.collision(level=self.level, block=around_player, windows_size=self.window_size, screen=self.screen,
                              game=self.game)

        self.player.pop(screen=self.screen)

        # Delete useless block
        for terrain_blocks in useless_terrain:
            self.terrain_block.__delitem__(terrain_blocks)

        if self.player.is_in_jump:
            self.player.jumping(game=self.game, level=self.level, screen=self.screen)
            if self.background_movement % 5 == 0:
                self.player.jumping(game=self.game, level=self.level, screen=self.screen)

        if self.player.is_auto_down:
            self.player.down(level=self.level, screen=self.screen)
            self.player.down(level=self.level, screen=self.screen)

    # End
    def end(self):
        pygame.mixer.music.stop()
        pygame.mouse.set_visible(True)
