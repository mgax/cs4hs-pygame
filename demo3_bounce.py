import random
import pygame


def main():
    screen_rect = pygame.Rect((0, 0), (640, 480))
    screen = pygame.display.set_mode(screen_rect.size)
    ball = pygame.Rect((0, 200), (40, 40))
    speed_x = 10

    while True:
        ball.move_ip(speed_x, 0)
        ball.clamp_ip(screen_rect)

        if ball.right == screen_rect.right:
            speed_x = -speed_x
        if ball.left == screen_rect.left:
            speed_x = -speed_x

        print ball
        screen.fill(pygame.Color('#ffffff'))
        pygame.draw.circle(screen, pygame.Color('#4444ff'), ball.center, 20)
        pygame.display.flip()

        pygame.time.wait(50)


if __name__ == '__main__':
    main()
