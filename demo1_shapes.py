import pygame


def main():
    screen = pygame.display.set_mode((640, 480))

    screen.fill(pygame.Color('#ffffff'))

    pygame.draw.circle(screen, pygame.Color('#ff8888'), (300, 200), 50)

    rect = pygame.Rect((100, 50), (100, 100))
    screen.fill(pygame.Color('#8888ff'), rect)

    logo = pygame.image.load('logo-header.png')
    logo_small = pygame.transform.smoothscale(logo, (100, 100))
    screen.blit(logo_small, (50, 300))

    pygame.display.flip()

    import time; time.sleep(10)


if __name__ == '__main__':
    main()
