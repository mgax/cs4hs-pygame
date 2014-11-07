import pygame


def main():
    x = 0

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))

    while True:
        x += 10
        screen.fill(pygame.Color('white'))
        pygame.draw.circle(screen, pygame.Color('blue'), (x, 300), 30)
        pygame.display.flip()
        clock.tick(30)


main()
