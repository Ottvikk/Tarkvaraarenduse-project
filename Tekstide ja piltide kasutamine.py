

import pygame
pygame.init()
#ekraani seaded
screen = pygame.display.set_mode([640, 480]) #Ekraani suuruse määramine
pygame.display.set_caption("Ülesanne 2") #Pealkirja määramine


#Lisame pildid
bg_shop = pygame.image.load("img/bg_shop.jpg") #Lisame pildi
screen.blit(bg_shop,[0,0]) #Pildi asukoht
bg_shop = pygame.transform.scale(bg_shop, [300, 120]) #Pildi suurus
seller = pygame.image.load("img/seller.jpg")#Lisame pildi
seller = pygame.transform.scale(seller, [200, 270])#Pildi asukoht
screen.blit(seller,[200,150])#Pildi suurus
chat = pygame.image.load("img/chat.jpg")#Lisame pildi
chat = pygame.transform.scale(chat, [250, 170])#Pildi asukoht
screen.blit(chat,[350,30])#Pildi suurus
font = pygame.font.Font(None, 25) #Teksti suurus
text = font.render("Tere, olen Ott-Saamuel Oja", True, [255,255,255]) #tekst
screen.blit(text, [360,100]) #Teksti asukoht
pygame.display.flip() #Keerab ekraani

running=True
#Tsükkel hakkab
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
