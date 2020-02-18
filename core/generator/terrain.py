import pygame


class Terrain:

    def __init__(self):
        self.texture = pygame.image.load("assets/textures/test_terrain.png")
        self.box = [25, 25]

    def pop(self, screen, position):
        screen.blit(self.texture, position)
        pygame.display.flip()
