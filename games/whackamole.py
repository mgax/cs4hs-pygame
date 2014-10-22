import random
import pygame


def main():
    screen_rect = pygame.Rect((0, 0), (640, 480))
    screen = pygame.display.set_mode(screen_rect.size)
    mole = pygame.Rect((0, 0), (40, 40))
    whack = pygame.Rect((0, 0), (10, 10))
    color = pygame.Color('#4444ff')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
		whack.center = pygame.mouse.get_pos()
                if mole.contains(whack):
                    x, y = random.randint(0, 640), random.randint(0, 480)		
                    mole.center = (x, y)
                    mole.clamp_ip(screen_rect)

        screen.fill(pygame.Color('#ffffff'))
        pygame.draw.circle(screen, color, mole.center, 20)
        pygame.display.flip()

        pygame.time.wait(50)


if __name__ == '__main__':
    main()
