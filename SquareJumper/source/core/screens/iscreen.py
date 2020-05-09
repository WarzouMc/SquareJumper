import pygame.sprite
from core.screens.element.ielement import Button, Text


def compare(position, size, position_):
    return (position[0] <= position_[0] <= position[0] + size[0]) and \
           (position[1] <= position_[1] <= position[1] + size[1])


# This is the Superclass for Screen
class Screen(pygame.sprite.Sprite):

    def __init__(self, element_list):
        super().__init__()
        self.element_list = element_list
        self.images = {}
        for element in self.element_list:
            if isinstance(element, Text):
                texture = element.get_texture()
            else:
                texture = pygame.image.load(element.get_texture_path()).convert_alpha()
            color = element.get_color()
            texture.fill((color[0], color[1], color[2]), special_flags=pygame.BLEND_MULT)
            self.images[element] = texture

    # Display the screen
    def show(self, screen):
        for element in self.element_list:
            texture = self.images.__getitem__(element)
            rect = texture.get_rect()
            position = element.get_position()
            rect.x = position[0]
            rect.y = position[1]
            screen.blit(texture, rect)

    # Action when click with mouse
    def on_click(self, game, where):
        for element in self.element_list:
            if isinstance(element, Button):
                image = self.images.__getitem__(element)
                size = image.get_size()
                rect = element.get_position()
                if compare(rect, size, where):
                    if element.get_name() == "play_button":
                        game.run_game(level=0)
                    elif element.get_name() == "menu_button":
                        game.show_menu()

    # Action when mouse moves
    def on_move_mouse(self, where):
        for element in self.element_list:
            if isinstance(element, Button):
                image = self.images.__getitem__(element)
                color = element.get_color()
                image.fill((color[0], color[1], color[2]), special_flags=pygame.BLEND_MAX)
                size = image.get_size()
                rect = element.get_position()
                if compare(rect, size, where):
                    over_color = element.get_over_color()
                    image.fill((over_color[0], over_color[1], over_color[2]), special_flags=pygame.BLEND_MULT)

    # Return all element
    def get_element_list(self):
        return self.element_list
