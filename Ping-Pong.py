
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
    screen.blit(ball, (posX, posY))
    screen.blit(pad, (posB, posA))
    posX += speedX
    posY += speedY
    posB += speedB
    posA += speedA
    # kui puudub ääri, siis muudab suunda

    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY

    if posA > screenX - pad.get_rect().width or posA < 0:
        speedA = -speedA

    if posB > screenY - pad.get_rect().height or posB < 0:
        speedB = -speedB

    if (ball.isTouching(pad)):
        {pad.setAnimation("bounce")}





    # graafika kuvamine ekraanil
    pygame.display.update()
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()
"""
import pygame, random
pygame.init()

#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)
clock = pygame.time.Clock()
posX, posY = 0, 0
speedX, speedY = 3, 4

#player
player = pygame.Rect(posX, posY, 120, 140)
playerImage = pygame.image.load("img/ball.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

#enemy - tekitame 5 suvalist vaenlast
enemies = []
for i in range(5):
    enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))
enemyImage = pygame.image.load('img/pad.png')
enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])


enemyCounter = 0
totalEnemies = 20
score = 0

gameover = False
while not gameover:
    clock.tick(60)
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    #player liikumine
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage,player)

    posX += speedX
    posY += speedY

    if posX > screenX-playerImage.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY-playerImage.get_rect().height or posY < 0:
        speedY = -speedY


    #enemy loomine
    enemyCounter += 1
    if enemyCounter >= totalEnemies:
        enemyCounter = 0
        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1

    for enemy in enemies:
        screen.blit(enemyImage, enemy)

    pygame.display.flip()
    screen.fill(lBlue)

    print(score)
    if score == 20:
        gameover = True
pygame.quit()
"""