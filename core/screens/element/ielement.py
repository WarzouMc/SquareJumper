import pygame


# This is the Superclass for all screen element
class ScreenElement:

    def __init__(self, texture_path, name, position, color):
        self.texture_path = texture_path
        self.name = name
        self.position = position
        self.color = color

    # Obtain the texture path
    def get_texture_path(self):
        return self.texture_path

    # Get name of this element
    def get_name(self):
        return self.name

    # Get the position
    def get_position(self):
        return self.position

    # Get the color
    def get_color(self):
        return self.color


# Superclass for Button
class Button(ScreenElement):

    def __init__(self, texture_path, name, position, color, over_color):
        super().__init__(texture_path=texture_path, name=name, position=position, color=color)
        self.over_color = over_color

    # Get over color (when mouse is above)
    def get_over_color(self):
        return self.over_color


# Superclass for Text
class Text(ScreenElement):

    def __init__(self, name, position, color, text, font, size):
        super().__init__(texture_path=None, name=name, position=position, color=color)
        self.text = text
        self.font = font
        self.size = size

        self.font = pygame.font.SysFont(self.font, self.size)
        self.texture = self.font.render(self.text, False, (color[0], color[1], color[2]))

    # Return texture
    def get_texture(self):
        return self.texture
