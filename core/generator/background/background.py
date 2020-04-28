from core.generator.background.ibackground import IBackground


class Backgrounds:

    def __init__(self):
        self.background_list = [
            Background001()
        ]


class Background001(IBackground):

    def __init__(self):
        super().__init__("assets/textures/background/background$0.png")