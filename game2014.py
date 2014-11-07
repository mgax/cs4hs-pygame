import pygame


def main():
    x = 0
    vx = 10
    world = pygame.Rect((0, 0), (800, 600))
    ball = pygame.Rect(world.center, (60, 60))

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))

    while True:
        ball.move_ip(vx, 0)
        ball.clamp_ip(world)
        if ball.right == world.right or ball.left == world.left:
            vx = -vx

        screen.fill(pygame.Color('white'))
        pygame.draw.circle(screen, pygame.Color('blue'), ball.center, 30)
        pygame.display.flip()
        clock.tick(30)


main()
