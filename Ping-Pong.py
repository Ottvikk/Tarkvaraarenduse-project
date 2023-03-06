
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
posA, posB = 320, 0
speedA, speedB = 0, 3.7





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

    if ball == padtl or ball == padtr:
        ball.get_rect().height


    # graafika kuvamine ekraanil
    pygame.display.update()
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()
