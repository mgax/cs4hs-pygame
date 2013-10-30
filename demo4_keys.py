import random
import pygame


def main():
    screen_rect = pygame.Rect((0, 0), (640, 480))
    screen = pygame.display.set_mode(screen_rect.size)
    ball = pygame.Rect((0, 200), (40, 40))
    speed_x = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            speed_y = 10
        elif pressed_keys[pygame.K_UP]:
            speed_y = -10
        else:
            speed_y = 0

        ball.move_ip(speed_x, speed_y)
        ball.clamp_ip(screen_rect)

        if ball.right == screen_rect.right:
            speed_x = -speed_x
        if ball.left == screen_rect.left:
            speed_x = -speed_x

        screen.fill(pygame.Color('#ffffff'))
        pygame.draw.circle(screen, pygame.Color('#4444ff'), ball.center, 20)
        pygame.display.flip()

        pygame.time.wait(50)


if __name__ == '__main__':
    main()
