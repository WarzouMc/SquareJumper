"""
This module is used to create IPlayer
"""
import core.player.iplayer


class Player(core.player.iplayer.IPlayer):

    def __init__(self):
        super().__init__(texture_path="assets/textures/player/player_texture$0.png")
        self.id = 1000
