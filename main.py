import pygame


class PlayerNinja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50

        self.image = pygame.image.load("graphics/Ninja.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        pass


pygame.init()
screen = pygame.display.set_mode((1000, 720))
pygame.display.set_caption('Ninja Dodgeball')
clock = pygame.time.Clock()
running = True

dojo_floor_surface = pygame.Surface.convert(pygame.image.load('graphics/hardwood.png'))
dfs = pygame.transform.scale(dojo_floor_surface, (1000, 720))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

    screen.blit(dfs, (0, 0))

    pygame.display.flip()

pygame.quit()



