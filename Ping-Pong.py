"""
import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]


# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

balls = []
score = 0

# graafika laadimine
ball = pygame.image.load("img/ball.png")
pad = pygame.image.load("img/pad.png")

padtr = print(pad.get_rect().topright)
padtl = print(pad.get_rect().topleft)
padbr = print(pad.get_rect().bottomright)
padbl = print(pad.get_rect().bottomleft)

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 7, 4
posA, posB = 350, 0
speedA, speedB = 0, 3

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # pildi lisamine ekraanile
    bal = pygame.Rect(posX, posY, 120, 140)
    screen.blit(ball, bal)
    screen.blit(pad, (posB, posA))
    pad = pygame.transform.scale(pad, [120,20])
    ball = pygame.transform.scale(ball,[20,20])
    posX += speedX
    posY += speedY
    posB += speedB
    posA += speedA

    # kui puudub ääri, siis muudab suunda

    if posX > screenX-ball.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY-ball.get_rect().height or posY < 0:
        speedY = -speedY

    if posA > screenX-pad.get_rect().width or posA < 0:
        speedA = -speedA

    if posB > screenY-pad.get_rect().height or posB < 0:
        speedB = -speedB



    # graafika kuvamine ekraanil
    pygame.display.update()
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()
"""
import pygame
import random

BALL_SPEED = int(input("Vali palli kiirus: ")) #mängija saab palli liikumiskiiruse määrata
BALL_SIZE = int(input("Vali palli suurus(vaikimisi 20): ")) #mängija saab palli suuruse määrata
WIDTH = 640 # laius
HEIGHT = 480 # kõrgus
FPS = 60 # fps määraja
ball = pygame.image.load("img/ball.png")
pad = pygame.image.load("img/pad.png")
BACKGROUND_COLOR = (240, 240, 240) # taustavärv
PADDLE_WIDTH = 120 # lauajupi laius
PADDLE_HEIGHT = 20 # lauajupi kõrgus
PADDLE_SPEED = 7 # lauajupi liikumiskiirus

# Initsialiseeri Pygame'i
pygame.init() # initsialiiserib
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #ekraani mood
pygame.display.set_caption("Pall ja alus mäng") #ekraani nimi
clock = pygame.time.Clock() #kell

# Mängu elemendid
screen.blit(ball,(100,100))
screen.blit(pad,(320,320))
ball_speed_x = BALL_SPEED * random.choice((1, -1)) #palli liikumine x teljel
ball_speed_y = BALL_SPEED * random.choice((1, -1)) #palli liikumine y teljel
paddle = pygame.Rect(WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT / 1.5, PADDLE_WIDTH, PADDLE_HEIGHT) #loob mängu kujundi palk
paddle_speed = 0 #palgi kiirus

# Mängu loop
running = True
score = 0
while running:
    # Sündmuste loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -PADDLE_SPEED
            elif event.key == pygame.K_RIGHT:
                paddle_speed = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speed = 0

    # Liiguta palli
    ball.x += ball_speed_x
    ball.y += ball_speed_y


    # Põrkumine seintega
    if ball.right >= WIDTH or ball.left <= 0:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= HEIGHT:
        score -= 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))

    # Põrkumine alusega
    if ball.colliderect(paddle) and ball_speed_y > 0:
        score += 1
        ball_speed_y *= -1

    # Liiguta alust
    paddle.x += paddle_speed
    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > WIDTH:
        paddle.right = WIDTH

    # Joonista ekraanile
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (0, 0, 0), paddle)
    pygame.draw.ellipse(screen, (0, 0, 0), ball)
    score_text = pygame.font.SysFont(None, 24).render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    # Piiritle FPS
    clock.tick(FPS)

# Lõpeta Pygame'i
pygame.quit()