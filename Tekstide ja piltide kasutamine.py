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
screen.fill([204, 255, 204])

#Lisame pildid
bg = pygame.image.load("img/bg_shop.jpg")
screen.blit(bg,[0,0])

pygame.display.flip()