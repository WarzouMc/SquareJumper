import ctypes

import pygame

from core.game import Game
from eventlistener import keyListener


def get_window_size(div=1.0):
    user = ctypes.windll.user32
    return int(user.GetSystemMetrics(78) / div), int(user.GetSystemMetrics(79) / div)


def start(size_div=1.0):
    pygame.init()
    size = width, height = get_window_size(size_div)
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Square Jumper')

    texturetest = pygame.image.load("assets/textures/test_terrain.png")
    recttest = [20, 40]

    running = True
    game = Game()
    game.generation(screen=screen, windows_size=size)
    while running:
        screen.fill(black)
        for terrain in game.terrain_block:
            terrain.pop(screen=screen)
        pygame.display.flip()
        if game.key.get(pygame.K_RIGHT):
            for terrain in game.terrain_block:
                terrain.move(screen=screen, add=[-2, 0])
        for event in pygame.event.get():
            keyListener.EventListener(event, game)


if __name__ == "__main__":
    screen_dimension_div = 1.5
    start(screen_dimension_div)
