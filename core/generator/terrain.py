import pygame


class Terrain:

    def __init__(self):
        self.texture = pygame.image.load("assets/textures/test_terrain.png")
        self.box = [3750, 75]
        self.bound = [0, 0]
        self.pos = [0, 0]

    def pop(self, screen, position):
        screen.blit(self.texture, position)
        self.bound = position
        pygame.display.flip()
        self.pos = position

    def move(self, screen, add):
        self.pos[0] += add[0]
        self.pos[1] += add[1]
        if self.pos[0] == 0 or self.pos[0] == -2500:
            self.pos[0] = -1250
        position = self.texture.get_rect().move(self.pos[0], self.pos[1])
        screen.blit(self.texture, position)
        pygame.display.update()
