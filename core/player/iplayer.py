import pygame
import asyncio

from core.generator.materials.imaterials import IMaterial


@asyncio.coroutine
async def jump_loop(power):
    async for i in range(10):
        await pygame.time.delay(10)
        print("test")


class IPlayer(IMaterial):

    def __init__(self):
        super().__init__()
        self.id = -1
        self.can_spawn = True
        self.is_in_jump = False

    def spawn(self, position, size):
        if self.can_spawn:
            return
        self.pop_gen(pos=position, size=size)

    def can_spawn(self):
        return self.can_spawn

    def jump(self, power):
        if not self.can_spawn:
            return
        jump_loop(power)
