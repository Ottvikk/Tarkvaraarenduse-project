import pygame
pygame.init()

ruut =  int(input('Mitu ruutu on vaja joonistada: '))
ruut_mõõtmed = int(input('Kui suur on ruudu külg: '))
print('valida saad värvide: punane/sinine/kollane/valge/must')
värv = input('Sisesta milist värvi soovid: ')

while  värv == punane or sinine or kolane or valge or must:



    screen =pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([83, 219, 120])



pygame.display.flip()

running=True
#Tsükkel hakkab
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False