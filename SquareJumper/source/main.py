import ctypes
import os
import pygame

from core.game import Game
from eventlistener import eventlistener


# Return div au window size
def get_window_size(div=1.0):
    user = ctypes.windll.user32
    return int(user.GetSystemMetrics(78) / div), int(user.GetSystemMetrics(79) / div)


# Start the program
def start(size_div=1.0):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    size = width, height = (25 * 50, 25 * 25)
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Square Jumper')

    running = True

    game = Game(screen, size)

    # Program loop
    while running:
        game.default_run()
        if game.get_level_runner() is not None:
            player = game.get_level_runner().player
            if not game.key.get(pygame.K_SPACE) and not player.is_auto_down and player.get_jump_core().is_charged_():
                y = player.get_position_y()
                player.jump(power=player.get_jump_core().get_jump_power(), last_y=y)
        for event in pygame.event.get():
            listen = eventlistener.listener(event=event, game=game)
            if isinstance(listen, eventlistener.MouseListener) and game.get_current_screen() is not None:
                if listen.get_type() == pygame.MOUSEBUTTONUP:
                    game.get_current_screen().on_click(game=game, where=listen.get_position())
                elif listen.get_type() == pygame.MOUSEMOTION:
                    game.get_current_screen().on_move_mouse(listen.get_position())


# Start
if __name__ == "__main__":
    screen_dimension_div = 1.5
    start(screen_dimension_div)
