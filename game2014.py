import pygame


def main():
    R = 30
    x = 0
    vx = 10
    vy = 10
    world = pygame.Rect((0, 0), (800, 600))
    ball = pygame.Rect(world.center, (2*R, 2*R))

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(world.size)

    while True:
        ball.move_ip(vx, vy)
        ball.clamp_ip(world)
        if ball.right == world.right or ball.left == world.left:
            vx = -vx
        if ball.top == world.top or ball.bottom == world.bottom:
            vy = -vy

        screen.fill(pygame.Color('white'))
        pygame.draw.circle(screen, pygame.Color('blue'), ball.center, R)
        pygame.display.flip()
        clock.tick(30)


main()
