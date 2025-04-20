from time import sleep
import pygame

def bouncy_ball_lol():
    global speed_x, speed_y, score1, score2
    ball.x += speed_x
    ball.y += speed_y
    if ball.colliderect(player1) or ball.colliderect(player2):
        speed_x *= -1
    if ball.bottom >= screen_y - 10 or ball.top <= 10:
        speed_y *= -1
    if ball.right >= screen_x - 10:
        score1 = score1 + 1
        ball.x = 300
        ball.y = 200
        speed_x, speed_y = 2, 1
        sleep(1)
        bouncy_ball_lol()
    if ball.left <= 10:
        score2 = score2 + 1
        ball.x = 300
        ball.y = 200
        sleep(1)
        bouncy_ball_lol()
    pygame.draw.rect(screen, (255, 255, 255), ball)


pygame.init()
pygame.display.set_caption("Pong")
icon = pygame.image.load("pixel-32x32.png")
pygame.display.set_icon(icon)
screen_x = 600
screen_y = 400
score1 = 0
score2 = 0
player1 = pygame.Rect((30, 150, 10, 100))
player2 = pygame.Rect((550, 150, 10, 100))
boundary1 = pygame.Rect((0, 0, 600, 10))
boundary2 = pygame.Rect((0, 390, 600, 10))
border1 = pygame.Rect((0, 10, 10, 380))
border2 = pygame.Rect((590, 10, 10, 380))
ball = pygame.Rect((300, 200, 10, 10))
text = pygame.font.Font("freesansbold.ttf", 32)
speed_x, speed_y = 2, 1
screen = pygame.display.set_mode((screen_x, screen_y))
run = True
while run:
    # slowin down movement
    sleep(0.01)
    pygame.display.update()
    # drawing stuff to screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), boundary1)
    pygame.draw.rect(screen, (255, 255, 255), boundary2)
    pygame.draw.rect(screen, (200, 200, 200), border1)
    pygame.draw.rect(screen, (200, 200, 200), border2)
    pygame.draw.rect(screen, (255, 255, 255), player1)
    pygame.draw.rect(screen, (255, 255, 255), player2)
    # rendering the score as text on screen
    player1_score = text.render(f"{score1}", True, (255, 255, 255))
    screen.blit(player1_score, (280, 10))

    player2_score = text.render(f"{score2}", True, (255, 255, 255))
    screen.blit(player2_score, (320, 10))

    bouncy_ball_lol()
    # input management
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player1.move_ip(0, -2)
    if key[pygame.K_DOWN]:
        player1.move_ip(0, 2)

    if key[pygame.K_w]:
        player2.move_ip(0, -2)
    if key[pygame.K_s]:
        player2.move_ip(0, 2)

    tolerance = 20  # collision tolerance
    if player1.colliderect(boundary1) or player1.colliderect(boundary2):
        if abs(boundary1.bottom - player1.top) < tolerance:
            player1.move_ip(0, 2)
        if abs(boundary2.top - player1.bottom) < tolerance:
            player1.move_ip(0, -2)
    if player2.colliderect(boundary1) or player2.colliderect(boundary2):
        if abs(boundary1.bottom - player2.top) < tolerance:
            player2.move_ip(0, 2)
        if abs(boundary2.top - player2.bottom) < tolerance:
            player2.move_ip(0, -2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
