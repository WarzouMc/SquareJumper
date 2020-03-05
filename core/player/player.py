import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.texture = pygame.image.load("assets/textures/player/player_texture$0.png")
        self.rect = self.texture.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.base_pos = [0, 0]
        self.up = True

    def spawn(self, screen, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.base_pos = position

    def pop(self, screen):
        screen.blit(self.texture, self.rect)

    def jump(self):
        if self.rect.y < self.base_pos[1] - 50:
            self.up = False
        if self.up:
            self.rect.y -= 1
        else:
            self.rect.y += 1

    def reset_jump(self):
        self.up = True

    def add_y(self):
        self.rect.y -= 1
