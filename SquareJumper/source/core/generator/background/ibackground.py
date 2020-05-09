import pygame.sprite


# IBackground class is the Superclass of Backgrounds
class IBackground(pygame.sprite.Sprite):

    def __init__(self, texture_path="assets/textures/default/default.png"):
        super().__init__()
        self.texture = pygame.image.load(texture_path).convert_alpha()
        self.color = [255, 143, 1]
        self.texture.fill((self.color[0], self.color[1], self.color[2]), special_flags=pygame.BLEND_MULT)
        self.rect = self.texture.get_rect()
        self.dimension = self.texture.get_size()
        self.current = [self.rect.x, self.rect.y]
        self.bB_rect = self.texture.get_rect()

    # Movement function
    def move(self, add):
        self.rect.x += add[0]
        self.rect.y += add[1]
        self.current[0] += add[0]
        self.current[1] += add[1]

    # Display function
    def pop(self, screen):
        self.reset(self.rect, False)
        screen.blit(self.texture, self.rect)
        self.pop_bB(screen)

    # Display function for the 2nd texture
    def pop_bB(self, screen):
        self.reset(self.bB_rect, True)
        self.bB_rect.x = self.dimension[0] + self.current[0]
        self.bB_rect.y = self.current[1]
        screen.blit(self.texture, self.bB_rect)

    # Replace one texture
    def reset(self, rect, reset_current):
        if rect.x + self.dimension[0] <= 0:
            rect.x = self.dimension[0]
            if reset_current:
                self.current = [-1, 0]
