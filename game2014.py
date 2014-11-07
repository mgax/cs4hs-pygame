import pygame


def main():
    R = 30
    x = 0
    vx = 0
    vy = 0
    world = pygame.Rect((0, 0), (800, 600))
    ball = pygame.Rect(world.center, (2*R, 2*R))

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(world.size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            ball.move_ip(0, 10)
        if pressed[pygame.K_UP]:
            ball.move_ip(0, -10)
        if pressed[pygame.K_RIGHT]:
            ball.move_ip(10, 0)
        if pressed[pygame.K_LEFT]:
            ball.move_ip(-10, 0)

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
