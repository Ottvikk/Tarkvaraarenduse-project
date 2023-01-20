import pygame #Impordime pygame
pygame.init()

screen = pygame.display.set_mode([640,480]) #Ekraani suuruse määramine
pygame.display.set_caption("Ülesanne 2") #Nime panemine ekraanile




running=True
# Hakkab tsükkel. Selle abil saab panna X ekraani kinni.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.flip()