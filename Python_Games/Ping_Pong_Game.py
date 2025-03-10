import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)
paddle1 = pygame.Rect(10, HEIGHT//2 - 40, 10, 80)
paddle2 = pygame.Rect(WIDTH-20, HEIGHT//2 - 40, 10, 80)
ball_speed = [3, 3]
paddle_speed = 5

run = True
while run:
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), paddle1)
    pygame.draw.rect(win, (255, 255, 255), paddle2)
    pygame.draw.ellipse(win, (255, 255, 255), ball)
    pygame.display.flip()
    
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    if ball.y <= 0 or ball.y >= HEIGHT - 15:
        ball_speed[1] *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: paddle1.y -= paddle_speed
    if keys[pygame.K_s]: paddle1.y += paddle_speed
    if keys[pygame.K_UP]: paddle2.y -=
