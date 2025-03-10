import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 60, 50, 50)
bullets = []
enemies = [pygame.Rect(random.randint(0, WIDTH-50), 50, 50, 50) for _ in range(5)]

run = True
while run:
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), player)
    for bullet in bullets:
        pygame.draw.rect(win, (255, 255, 255), bullet)
        bullet.y -= 5
    for enemy in enemies:
        pygame.draw.rect(win, (255, 0, 0), enemy)
        enemy.y += 1
    bullets = [b for b in bullets if b.y > 0]
    pygame.display.flip()

    keys = pygame.key
