"""
This module allow to create IScreen
"""
from core.screens.iscreen import Screen
from core.screens.element.element import PlayButton
from core.screens.element.element import MenuButton
from core.screens.element.element import Point
from core.screens.element.element import DeathMessage
from core.screens.element.element import LevelComplete


class Menu(Screen):

    def __init__(self):
        super().__init__(element_list=[PlayButton()])


class DeathMenu(Screen):

    def __init__(self, point, cause):
        super().__init__(element_list=[PlayButton(), MenuButton(), Point(point), DeathMessage(cause)])


class WinMenu(Screen):

    def __init__(self, point, level):
        super().__init__(element_list=[PlayButton(), MenuButton(), Point(point), LevelComplete(level)])