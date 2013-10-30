import random
import pygame


def main():
    screen_rect = pygame.Rect((0, 0), (640, 480))
    screen = pygame.display.set_mode(screen_rect.size)
    ball = pygame.Rect((0, 0), (40, 40))
    color = pygame.Color('#4444ff')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                color = pygame.Color(
                    random.randint(1, 255),
                    random.randint(1, 255),
                    random.randint(1, 255),
                )

        ball.center = pygame.mouse.get_pos()
        ball.clamp_ip(screen_rect)

        screen.fill(pygame.Color('#ffffff'))
        pygame.draw.circle(screen, color, ball.center, 20)
        pygame.display.flip()

        pygame.time.wait(50)


if __name__ == '__main__':
    main()
