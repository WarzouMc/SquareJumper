import pygame.sprite


class IBackground(pygame.sprite.Sprite):

    def __init__(self, texture_path="assets/textures/default/default.png"):
        super().__init__()
        self.texture = pygame.image.load(texture_path).convert_alpha()
        self.rect = self.texture.get_rect()
        self.dimension = self.texture.get_size()
        self.current = [self.rect.x, self.rect.y]
        self.aA_rect = self.texture.get_rect()
        self.aB_rect = self.texture.get_rect()
        self.bB_rect = self.texture.get_rect()
        self.cA_rect = self.texture.get_rect()
        self.cB_rect = self.texture.get_rect()

    def move(self, add):
        self.rect.x += add[0]
        self.rect.y += add[1]
        self.current[0] += add[0]
        self.current[1] += add[1]

    def pop(self, screen):
        self.reset(self.rect, False)
        screen.blit(self.texture, self.rect)
        self.pop_aA(screen)
        self.pop_aB(screen)
        self.pop_bB(screen)
        self.pop_cA(screen)
        self.pop_cB(screen)

    def pop_aA(self, screen):
        self.reset(self.aA_rect, True)
        self.aA_rect.x = self.current[0]
        self.aA_rect.y = self.dimension[1] + self.current[1]
        screen.blit(self.texture, self.aA_rect)

    def pop_aB(self, screen):
        self.reset(self.aB_rect, True)
        self.aB_rect.x = self.dimension[0] + self.current[0]
        self.aB_rect.y = self.dimension[1] + self.current[1]
        screen.blit(self.texture, self.aB_rect)

    def pop_bB(self, screen):
        self.reset(self.bB_rect, True)
        self.bB_rect.x = self.dimension[0] + self.current[0]
        self.bB_rect.y = self.current[1]
        screen.blit(self.texture, self.bB_rect)

    def pop_cA(self, screen):
        self.reset(self.cA_rect, True)
        self.cA_rect.x = self.current[0]
        self.cA_rect.y = -self.dimension[1] + self.current[1]
        screen.blit(self.texture, self.cA_rect)

    def pop_cB(self, screen):
        self.reset(self.cB_rect, True)
        self.cB_rect.x = self.dimension[0] + self.current[0]
        self.cB_rect.y = -self.dimension[1] + self.current[1]
        screen.blit(self.texture, self.cB_rect)

    def reset(self, rect, reset_current):
        if rect.x + self.dimension[0] <= 0:
            rect.x = self.dimension[0]
            if reset_current:
                self.current = [-1, 0]
