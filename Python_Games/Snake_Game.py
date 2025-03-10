import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
snake_pos = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10]
direction = "RIGHT"

def move():
    global food_pos
    head = snake_pos[0][:]
    if direction == "UP":
        head[1] -= 10
    elif direction == "DOWN":
        head[1] += 10
    elif direction == "LEFT":
        head[0] -= 10
    elif direction == "RIGHT":
        head[0] += 10
    snake_pos.insert(0, head)
    if head == food_pos:
        food_pos = [random.randint(0, WIDTH // 10) * 10, random.randint(0, HEIGHT // 10) * 10]
    else:
        snake_pos.pop()

run = True
while run:
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.flip()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    move()

pygame.quit()
