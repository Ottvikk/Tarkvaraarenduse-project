
import pygame,random,sys #Impordib pygame'i, random'i ja sys'i

#Erinevad värvid
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

pygame.init()
screen = pygame.display.set_mode([640, 480]) #Ekraani seaded ja skoori seis
pygame.display.set_caption("Death Rally")
clock = pygame.time.Clock()
score = 0

bg = pygame.image.load("img/bg_rally.jpg")#Piltide mängu lisamine
bg = pygame.transform.scale(bg, [640, 480])
bgX = 0
blue1 = pygame.image.load("img/f1_blue.png")
blue2 = blue1
red = pygame.image.load("img/f1_red.png")

Blue1Y, Blue1X = random.randint(0, 100), random.randint(130, 460)#Siniste autode X ja Y koordinaadid
Blue2Y, Blue2X = random.randint(0, 100), random.randint(130, 460)
RedX, RedY = 300, 390  #Punase auto koordinaadid

Bspeed = 3   #Siniste autode kiirus

gameover = False
while not gameover:  #See on While-tsükklis nii kaua kuni mäng on läbi
    clock.tick(120)  # FPS
    for event in pygame.event.get():#Selle abil saab akent ristist kinni panna
        if event.type == pygame.QUIT:
            sys.exit()

    #Taustapildi lisamine mängu
    screen.blit(bg, (0, 0))

    #Siniste autode lisamine mängu ning nende asukoha panemine

    screen.blit(red, (RedX, RedY))#Punase auto mängu lisamine
    Blue1Y += Bspeed + random.randint(1,3) + 0.5#Siniste autode liikumiseks valmistuv kiiruse sättimine
    Blue2Y += Bspeed + random.randint(1,3)

    screen.blit(pygame.font.Font(None, 28).render(f"Score: {score}", True, [255,255,255]), [0,0]) #Skoori näitamiseks valmistuv rida

    if Blue1Y >= 480: #Need read annavad sinistele autodele võimaluse liikuda algusesse kui need jõuavad lõppu.
        Blue1Y = -120
        score += 1
        Blue1X = random.randint(130, 460)

    if Blue2Y >= 480:
        Blue2Y = -120
        score += 1
        Blue2X = random.randint(130, 460)

    key = pygame.key.get_pressed()  #Nende ridade abil saab vajutada punasel auto liikusmiseks klahve
    if key[pygame.K_LEFT]:  #Nüüd saab liikuda vasakule
        RedX -= 5  # Kui kiiresti saab auto liigub vasakule
    if key[pygame.K_RIGHT]:  #Nüüd saab liigutada paremale
        RedX += 5  #Kui kiiresti saab auto liigutada paremale

    #Näitab kuidas mäng võib läbi saada
    if RedY + 55 >= Blue1Y >= RedY - 55:
        if RedX + 50 >= Blue1X >= RedX - 50:
            gameover = True #Mängu lõpp
    if RedY + 55 >= Blue2Y>= RedY - 55:
        if RedX+ 50 >= Blue2X >= RedX - 50:
            gameover = True  #Mängu lõpp

    pygame.display.update() #Uendab mängu ja näitab pilti
while True: #While tsükkel algab kui mäng saab läbi
    if gameover:
        screen.blit(pygame.font.Font(None, 35).render("Game over!", True, [213, 50, 80]), [230, 300]) # Prindib ekraanile et mäng sai läbi
        screen.blit(pygame.font.Font(None, 35).render(f"Your Score is: {score}", True, [213, 50, 80]),# Saab printida enda tulemust selle mängu lõppus
                    [210, 200])
        pygame.display.update()  # Uuendab mängu ja näitab pilti

    for event in pygame.event.get():#Selle tsükkli abil saab seda mängu kinni panna
        if event.type == pygame.QUIT:
            sys.exit()