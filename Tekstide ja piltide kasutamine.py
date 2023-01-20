"""
import pygame #Impordime pygame
pygame.init()

screen = pygame.display.set_mode([640,480]) #Ekraani suuruse määramine
pygame.display.set_caption("Ülesanne 2") #Nime panemine ekraanile

bg = pygame.image.load("bg_shop.jpg")
screen.blit(bg,[0,0])



running=True
# Hakkab tsükkel. Selle abil saab panna X ekraani kinni.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.flip()
"""
import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")


#Lisame pildid
bg_shop = pygame.image.load("img/bg_shop.jpg")
screen.blit(bg_shop,[0,0])
bg_shop = pygame.transform.scale(bg_shop, [300, 120])
seller = pygame.image.load("img/seller.jpg")
seller = pygame.transform.scale(seller, [200, 270])
screen.blit(seller,[200,150])
chat = pygame.image.load("img/chat.jpg")
chat = pygame.transform.scale(chat, [250, 170])
screen.blit(chat,[350,30])
font = pygame.font.Font(None, 25)
text = font.render("Tere, olen Ott-Saamuel Oja", True, [255,255,255])
screen.blit(text, [360,100])
pygame.display.flip()

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
