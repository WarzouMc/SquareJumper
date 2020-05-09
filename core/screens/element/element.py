"""
This module is used to create new ScreenElement
"""
from core.screens.element.ielement import ScreenElement
from core.screens.element.ielement import Button
from core.screens.element.ielement import Text


class PlayButton(Button):

    def __init__(self):
        super().__init__(texture_path="assets/textures/screens/buttons/menu/play_button_off.png", name="play_button",
                         position=[500, 156], color=[255, 255, 0], over_color=[255, 0, 255])


class MenuButton(Button):

    def __init__(self):
        super().__init__(texture_path="assets/textures/screens/buttons/menu/menu_button.png", name="menu_button",
                         position=[500, 306], color=[255, 0, 255], over_color=[0, 255, 255])


class Point(Text):

    def __init__(self, point):
        super().__init__(name="point", position=[100, 100], color=[100, 255, 100], text="Points : " + str(point),
                         font="Arial", size=40)


class DeathMessage(Text):

    def __init__(self, cause):
        if cause == 3:
            self.text = "Ouch, you have took a wall !"
        elif cause == 4:
            self.text = "Oof, my butt !"
        elif cause == 6:
            self.text = "Hey, ..., my head !"

        super().__init__(name="point", position=[100, 150], color=[255, 50, 100], text=self.text,
                         font="Arial", size=30)


class LevelComplete(Text):

    def __init__(self, level):
        super().__init__(name="completed_level", position=[100, 150], color=[100, 100, 255],
                         text="You successfully the level " + str(level + 1), font="Arial", size=30)
