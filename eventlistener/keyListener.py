import sys

import pygame


class EventListener:
    def __init__(self, event, game):
        self.listener(self, event, game)

    @staticmethod
    def listener(self, event, game):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print('test')
            game.key[event.key] = True
        elif event.type == pygame.KEYUP:
            game.key[event.key] = False
        return event
