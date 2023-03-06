
import pygame, random, sys

screenX = 640
screenY = 480
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Death rally")
clock = pygame.time.Clock()
score = 0

bg_rally = pygame.image.load("img/bg_rally.jpg")
f1_red = pygame.image.load("img/f1_red.png")
f1_blue = pygame.image.load("img/f1_blue.png")
blue1 = f1_blue
blue2 = f1_blue


RedX, RedY = 300, 370

gameover = False
while not gameover:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    coords = []
    for i in range(10):
        Blue1X, Blue1Y = random.randint(130, 460), random.randint(0, 100)
        Blue2X, Blue2Y = random.randint(130, 460), random.randint(0, 100)
        Bspeed = random.randint(1, 5)
        coords.append([Blue1X,Blue1Y,Bspeed])

    # loendist koordinaadid
    for i in range(len(coords)):
        coords[i][1] += 1
        # kui jõuab alla, siis muudame ruduu alguspunkti
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(130, 460)
            coords[i][0] = random.randint(0, screenX)

    screen.blit(bg_rally, [0, 0])
    screen.blit(blue1, (Blue1X, Blue1Y))
    screen.blit(blue2, (Blue2X, Blue2Y))
    screen.blit(f1_red, (RedX, RedY))
    pygame.display.update()

pygame.quit()
"""
import pygame, sys, random

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
pygame.display.set_caption("Death Rally")
bg_rally = pygame.image.load("img/bg_rally.jpg")
clock = pygame.time.Clock()
f1_red = pygame.image.load("img/f1_red.png")
f1_blue = pygame.image.load("img/f1_blue.png")
blue1 = f1_blue
blue2 = f1_blue

Bspeed = 5

Blue1X, Blue1Y = random.randint(130,460), random.randint(0,100)
Blue2X, Blue2Y = random.randint(130,460), random.randint(0,100)
RedX, RedY = 300, 370

# koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(10):
    posX = random.randint(130,460)
    posY = random.randint(0,100)
    coords.append([posX, posY])


gameover = False
while not gameover:
    # fps
    clock.tick(120)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # loendist koordinaadid
    for i in range(len(coords)):
        screen.blit(bg_rally, [0, 0])
        screen.blit(blue1, (Blue1X, Blue1Y))
        screen.blit(blue2, (Blue2X, Blue2Y))
        screen.blit(f1_red, (RedX, RedY))
        coords[i][1] += 1
        # kui jõuab alla, siis muudame ruduu alguspunkti
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(0, screenX)

    pygame.display.flip()

pygame.quit()
"""