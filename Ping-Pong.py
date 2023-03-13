
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

screenX = 640 #Ekraani seaded
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()
score = 0



posX, posY = 0, 0       #Palli kiirus ja asukoht
speedX, speedY = 7, 6
speedA, speedB = 5,0   #Palgi kiirus ja asukoht
posA,posB = 0,350


ball = pygame.image.load("img/ball.png")#Palli mängu toomine, palli suurus ja kiirus
ball = pygame.transform.scale(ball, [20,20])
ball_rect = pygame.Rect(posX,posY,20,20)
pad = pygame.image.load("img/pad.png") #Palgi mängu toomine, palgi suurus ja kiirus
pad = pygame.transform.scale(pad, [120,20])
pad_rect = pygame.Rect(posA,posB,120,20)


gameover = False
while not gameover:#Mängu algus ja tsükkli algus
    clock.tick(90) #fps
    events = pygame.event.get() #Selle abil saab mängu risti kinni panna
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.blit(ball, (posX, posY)) #Palli ja palgi ekraanile toomine
    screen.blit(pad, (posA, posB))
    pall = pygame.Rect(posX,posY,20,20)
    pad_rect = pygame.Rect(posA, posB, 120, 20)

    posX += speedX #Palli ja palgi liigutamine
    posY += speedY
    posA += speedA
    posB += speedB

    screen.blit(pygame.font.Font(None, 30).render(f"Score: {score}", True, [255, 255, 255]), #Tulemuse näitamine ekraanil
                [10, 20])

    if posX > screenX - ball.get_rect().width or posX < 0: #Kui pall puutub ääri siis see põrkab
        speedX = -speedX
    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
    if posY > screenY -ball.get_rect().height: #Kui pall puuutub alumist äärt siis läheb punkt maha
        score-=1
    if posA > screenX - pad.get_rect().width or posA < 0: #Kui palk puutub seina siis see põrkab ja liigub alguse poole
        speedA = -speedA

    if pall.colliderect(pad_rect) and speedY > 0: #Kui pall puutb palki siis tuleb 1 punkt juurda ja pall põrkab
        speedY = -speedY
        score +=1

    pygame.display.update() #Uuendab ekraani
    screen.fill(lBlue) #Muudab tausta värvi.
    if score < -10: #Kui score muutub võiksemaks kui -10 siis see sulgub automaatselt
        pygame.quit()
pygame.quit()
