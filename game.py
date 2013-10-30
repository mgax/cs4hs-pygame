import pygame

SCREEN_SIZE = (640, 480)
SPEED = 5
BALL_SIZE = 20


def translate(pos, delta):
    return (pos[0] + delta[0], pos[1] + delta[1])


def main():
    screen_rect = pygame.Rect((0, 0), SCREEN_SIZE)
    screen = pygame.display.set_mode(screen_rect.size)
    color = pygame.Color('#ffff00')
    pos = pygame.Rect((0, 0), (BALL_SIZE, BALL_SIZE))
    pos.center = screen_rect.center

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            pos.move_ip(SPEED, 0)
        if pressed_keys[pygame.K_LEFT]:
            pos.move_ip(-SPEED, 0)
        if pressed_keys[pygame.K_DOWN]:
            pos.move_ip(0, SPEED)
        if pressed_keys[pygame.K_UP]:
            pos.move_ip(0, -SPEED)

        pos.clamp_ip(screen_rect)

        screen.fill(pygame.Color('#000000'))
        pygame.draw.circle(screen, color, pos.center, BALL_SIZE / 2)
        pygame.display.flip()
        pygame.time.wait(50)


if __name__ == '__main__':
    main()
