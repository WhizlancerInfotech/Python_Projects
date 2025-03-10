import pygame

pygame.init()
WIDTH, HEIGHT = 400, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_y = HEIGHT // 2
velocity = 0
gravity = 1
jump = -10

run = True
while run:
    win.fill((135, 206, 250))
    pygame.draw.circle(win, (255, 255, 0), (100, bird_y), 15)
    pygame.display.flip()
    clock.tick(30)

    velocity += gravity
    bird_y += velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity = jump

pygame.quit()
