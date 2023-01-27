"""
import pygame
pygame.init()
#screen=pygame.display.set_mode([640,480])
#screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)
pygame.display.set_caption("My Screen")
screen.fill([204, 255, 255])
#pygame.draw.line(screen, [255,0,0], [100,100], [220,220], 2) #joon
#pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2) #ristkülik
#pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1) #ring
#pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2) #hulknurk
#pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2) #ovaal
#pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1) #kaar
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
"""

import pygame #Impordime pygame
pygame.init()

screen = pygame.display.set_mode([300,500]) #Ekraani suuruse määramine
pygame.display.set_caption("Foor - Ott-Saamuel Oja") #Nime panemine ekraanile
pygame.draw.rect(screen, [126, 128, 130], [90, 10, 110, 280], 2) #Joonistame Vajalikud kujundid et tuleks õige pilt
pygame.draw.circle(screen, [7, 222, 39], [145,240], 40, 0)
pygame.draw.circle(screen, [240, 228, 7], [145,150], 40, 0)
pygame.draw.circle(screen, [240, 7, 7], [145,65], 40, 0)
pygame.draw.line(screen, [126,128,130], [145,290], [145,390], 2)
pygame.draw.polygon(screen, [126, 128, 130], [[100,390],[190,390],[250,450],[40,450],[100,390]], 2)
pygame.draw.polygon(screen, [0, 123, 255], [[100,390],[190,390],[210,410],[80,410],[100,390]], 0)
pygame.draw.polygon(screen, [3, 3, 3], [[80,410],[210,410],[230,430],[60,430],[80,410]], 0)
pygame.draw.polygon(screen, [255, 255, 255], [[60,430],[230,430],[250,450],[40,450],[60,430]], 0)
pygame.display.flip() #Põõrab ekraani ümber.


running=True
# Hakkab tsükkel. Selle abil saab panna X ekraani kinni.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
