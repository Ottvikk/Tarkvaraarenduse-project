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
import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
white = [255,255,255]
black = [0,0,0]


# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)  # täidab tausta valitud värviga
clock = pygame.time.Clock()

score = 0


# kiirus ja asukoht
posX, posY = 0, 0       #palli algne positsioon
speedX, speedY = 7, 6   #palli x ja y kiirused
aspeedX, aspeedY = 5,0  #palgi x ja y kiirused
pposX,pposY = 0,350   #palgi algne positsioon

# palli ja puulaua piltide ja suuruste lisamine
ball = pygame.image.load("img/ball.png")
ball = pygame.transform.scale(ball, [20,20])
ball_rect = pygame.Rect(posX,posY,20,20)
pad = pygame.image.load("img/pad.png")
pad = pygame.transform.scale(pad, [120,20])
pad_rect = pygame.Rect(pposX,pposY,120,20)


gameover = False
#alustab mängu tsükli ning lisab selle sisse mängu komponendid
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
    screen.blit(pad, (pposX, pposY))
    pall = pygame.Rect(posX,posY,20,20)
    pad_rect = pygame.Rect(pposX, pposY, 120, 20)

    # palli liikuma panemine
    posX += speedX
    posY += speedY
    pposX += aspeedX
    pposY += aspeedY

    #Score
    screen.blit(pygame.font.Font(None, 30).render(f"Score: {score}", True, [255, 255, 255]),
                [10, 20])  # skoori kuvamine
    # kui puudub ääri, siis muudab suunda
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX #teeb kiirusest negatiivse kiiruse
    #kui palli positsioon on suurem kui screenX siis see läheb kuhugi muusse suunda
    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
    #kui pall läheb palgist mööda siis läheb punkt skoorist maha
    if posY > screenY -ball.get_rect().height:
        score-=1
    # kui palgi positsioon on suurem kui screenY siis see läheb vasakule ja paremale
    if pposX > screenX - pad.get_rect().width or pposX < 0:
        aspeedX = -aspeedX

    # kui pall puutub palki siis see põrkab ning lisab skoori
    if pall.colliderect(pad_rect) and speedY > 0:
        speedY = -speedY
        score +=1

    pygame.display.flip()#värskendab ekraani
    screen.fill(lBlue)#täidab tausta valitud värviga

pygame.quit()
