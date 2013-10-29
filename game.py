import time
import pygame

SIZE_X = 640
SIZE_Y = 480
SPEED = 3


def translate(pos, delta):
    return (pos[0] + delta[0], pos[1] + delta[1])


class game:
    pos = (SIZE_X / 2, SIZE_Y / 2)


def main():
    game.screen = pygame.display.set_mode((SIZE_X, SIZE_Y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed_keys = pygame.key.get_pressed()
        new_pos = game.pos
        if pressed_keys[pygame.K_RIGHT]:
            new_pos = translate(new_pos, (SPEED, 0))
        if pressed_keys[pygame.K_LEFT]:
            new_pos = translate(new_pos, (-SPEED, 0))
        if pressed_keys[pygame.K_DOWN]:
            new_pos = translate(new_pos, (0, SPEED))
        if pressed_keys[pygame.K_UP]:
            new_pos = translate(new_pos, (0, -SPEED))

        if 0 < new_pos[0] < SIZE_X and 0 < new_pos[1] < SIZE_Y:
            game.pos = new_pos

        game.screen.fill(pygame.Color('#000000'))
        pygame.draw.circle(game.screen, pygame.Color('#ffff00'), game.pos, 5)
        pygame.display.flip()
        pygame.time.wait(15)


if __name__ == '__main__':
    main()
