import pygame


class PlayerNinja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.x = 50
        self.y = 50

        self.image = pygame.Surface([50, 50])
        self.image.fill('green')

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


def game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 720))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill('purple')

        ###

        pygame.display.flip()



game()
