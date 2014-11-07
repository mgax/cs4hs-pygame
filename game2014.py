import pygame


def main():
    screen = pygame.display.set_mode((800, 600))
    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('blue'), (400, 300), 30)
    pygame.display.flip()
    pygame.time.wait(1000)


main()
