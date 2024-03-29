
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
high_score = 0

with open('high_score.txt', 'r') as file:
    high_score = int(file.read())

posX, posY = 0, 0       #Palli kiirus ja asukoht
speedX, speedY = 7, 7
speedA, speedB = 5,0   #Palgi kiirus ja asukoht
posA,posB = 0,350


ball = pygame.image.load("ball.png")#Palli mängu toomine, palli suurus ja kiirus
ball = pygame.transform.scale(ball, [20,20])
ball_rect = pygame.Rect(posX,posY,20,20)
pad = pygame.image.load("pad.png") #Palgi mängu toomine, palgi suurus ja kiirus
pad = pygame.transform.scale(pad, [120,20])
pad_rect = pygame.Rect(posA,posB,120,20)

pygame.mixer.music.load('Music.mp3')
Sound = pygame.mixer.Sound('Sound.wav')
pygame.mixer.Sound.set_volume(Sound,1)
Effect = pygame.mixer.Sound('effect.wav')
pygame.mixer.Sound.set_volume(Effect,1)
pygame.mixer.music.play(-3)
taust = pygame.image.load("City.jpg")
taust = pygame.transform.scale(taust, [640, 640])

gameover = False
while not gameover:#Mängu algus ja tsükkli algus
    clock.tick(90) #fps
    events = pygame.event.get() #Selle abil saab mängu risti kinni panna
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    screen.blit(taust,(0,0))
    screen.blit(ball, (posX, posY)) #Palli ja palgi ekraanile toomine
    screen.blit(pad, (posA, posB))
    pall = pygame.Rect(posX,posY,20,20)
    pad_rect = pygame.Rect(posA, posB, 120, 20)

    posX += speedX #Palli ja palgi liigutamine
    posY += speedY

    move = pygame.key.get_pressed() #Selle abil saab palki liigutada klahvidega
    if move[pygame.K_LEFT]: #Vasakule
        posA -= 4
    if move[pygame.K_RIGHT]: #Paremale
        posA += 4
    screen.blit(pygame.font.Font(None, 30).render(f"Score: {score}", True, [255, 255, 255]), #Tulemuse näitamine ekraanil
                [10, 20])

    if posX > screenX - ball.get_rect().width or posX < 0: #Kui pall puutub ääri siis see põrkab
        speedX = -speedX
        pygame.mixer.Sound.play(Effect)
    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
        pygame.mixer.Sound.play(Effect)
    if posY > screenY -ball.get_rect().height: #Kui pall puuutub alumist äärt siis läheb punkt maha
        score-=1
        pygame.mixer.Sound.play(Effect)
    if posA > screenX - pad.get_rect().width or posA < 0: #Kui palk puutub seina siis see põrkab ja liigub alguse poole
        speedA = -speedA

    if pall.colliderect(pad_rect) and speedY > 0: #Kui pall puutb palki siis tuleb 1 punkt juurda ja pall põrkab
        speedY = -speedY
        score +=1
        pygame.mixer.Sound.play(Sound)
    pygame.display.update() #Uuendab ekraani
    screen.fill(lBlue) #Muudab tausta värvi.
    if score < -10: #Kui score muutub võiksemaks kui -10 siis see sulgub automaatselt
        pygame.quit()
pygame.quit()