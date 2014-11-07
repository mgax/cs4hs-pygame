import pygame


def main():
    pygame.font.init()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 28)
    R = 30
    FOOD_R = 10
    x = 0
    vx = 10
    vy = 10
    score = 0
    world = pygame.Rect((0, 0), (800, 600))
    ball = pygame.Rect(world.center, (2*R, 2*R))
    food = None

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(world.size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                food = pygame.Rect((0, 0), (FOOD_R*2, FOOD_R*2))
                food.center = event.pos

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

        if food and ball.colliderect(food):
            score += 100
            food = None

        screen.fill(pygame.Color('white'))
        pygame.draw.circle(screen, pygame.Color('blue'), ball.center, R)
        if food:
            pygame.draw.circle(screen, pygame.Color('red'), food.center, FOOD_R)
        text = font.render("score: %d" % score, True, pygame.Color('black'))
        screen.blit(text, (0, 0))
        pygame.display.flip()
        clock.tick(30)


main()
