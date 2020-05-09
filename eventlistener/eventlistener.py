"""
This module manage key and mouse events
"""
import sys

import pygame


# Listen events
def listener(event, game):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        return KeyListener(game, True, event)
    elif event.type == pygame.KEYUP:
        return KeyListener(game, False, event)
    elif event.type == pygame.MOUSEMOTION:
        return MouseListener(game, event.type)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        return MouseListener(game, event.type)
    elif event.type == pygame.MOUSEBUTTONUP:
        return MouseListener(game, event.type)
    return event


# Manage key event
class KeyListener:

    def __init__(self, game, press, event):
        self.game = game
        self.press = press
        self.event = event

        self.game.key[event.key] = self.press

    # Return true if the key is press
    def is_pressed_key(self):
        return self.press

    # Return event
    def get_event(self):
        return self.event

    # Return key
    def get_key(self):
        return self.event.key


# Manage mouse event
class MouseListener:

    def __init__(self, game, type_):
        self.game = game
        self.type_ = type_

    # Return type
    def get_type(self):
        return self.type_

    # Return mouse position
    @staticmethod
    def get_position():
        return pygame.mouse.get_pos()

    # Return mouse
    @staticmethod
    def get_mouse():
        return pygame.mouse
