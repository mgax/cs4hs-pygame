import pygame


def main():
    screen = pygame.display.set_mode((800, 600))
    screen.fill(pygame.Color('white'))
    pygame.display.flip()
    pygame.time.wait(1000)


main()
