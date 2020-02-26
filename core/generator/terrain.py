import pygame


class Terrain(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.texture = pygame.image.load("assets/textures/test_terrain.png")
        self.rect = self.texture.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.base_rect = [0, 0]
        self.size = (0, 0)

    def pop_gen(self, pos, size):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.base_rect[0] = pos[0]
        self.base_rect[1] = pos[1]
        self.size = size

    def pop(self, screen):
        screen.blit(self.texture, self.rect)

    def move(self, screen, add):
        self.rect.x += add[0]
        if self.rect.x <= -50:
            self.rect.x = self.size[0]
