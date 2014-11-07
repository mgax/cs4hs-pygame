import pygame


def main():
    x = 0
    vx = 10

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))

    while True:
        x += vx
        if x > 800:
            x = 800
            vx = -vx
        if x < 0:
            x = 0
            vx = -vx

        screen.fill(pygame.Color('white'))
        pygame.draw.circle(screen, pygame.Color('blue'), (x, 300), 30)
        pygame.display.flip()
        clock.tick(30)


main()
