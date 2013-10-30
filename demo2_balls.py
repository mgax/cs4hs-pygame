import random
import pygame


def main():
    screen = pygame.display.set_mode((640, 480))

    screen.fill(pygame.Color('#ffffff'))

    rect = pygame.Rect((100, 50), (300, 300))
    screen.fill(pygame.Color('#8888ff'), rect)

    for c in range(100):
        pos = (random.randint(0, 640), random.randint(0, 480))
        #pygame.draw.circle(screen, pygame.Color('#ff8888'), pos, 20)
        ball_rect = pygame.Rect((pos[0] - 20, pos[1] - 20), (40, 40))
        #if rect.colliderect(ball_rect):
        if rect.contains(ball_rect):
            color = pygame.Color('#88ff88')
        else:
            color = pygame.Color('#ff8888')
        pygame.draw.circle(screen, color, pos, 20)

    pygame.display.flip()

    import time; time.sleep(10)


if __name__ == '__main__':
    main()
