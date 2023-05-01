import pygame


def game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 720))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill('purple')
        pygame.display.flip()


game()
