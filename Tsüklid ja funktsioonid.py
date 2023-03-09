
import pygame #Impordib pygame'i

punane = [255, 0, 0] #Värvid
kollane = [255, 255, 51]
sinine = [0, 0, 255]
valge = [0, 0, 0]
must = [255, 255, 255]

pygame.display.set_caption("Ruudud")
screen = pygame.display.set_mode([640, 480]) #Ekraani seaded

screen.fill(punane) #Ekraani värvi muutmine

class ruut: #Teeme klassi nimega ruut sest selle abil me teeme ruudud
    def __init__(self, color, esimene, teine): #Defineerime self'i, color'i, esimese ja teise
        self.color = color
        self.esimene = esimene
        self.teine = teine

    def make_square(self): #Defineerime sõna make_square
        y = 1
        for i in range(35):
            x = 1
            for j in range(38):
                pygame.draw.rect(screen, self.color, [x, y, self.esimene, self.teine])
                x += 18
            y += 18

ruut.make_square(ruut(sinine, 16, 16)) #Joonistab ruudud

pygame.display.update() #Uuendab ekraani

running = True #Tsükkel mis hoiab kasutajal pilti ees
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update() #Uuendab ekraani

pygame.quit() #Kinni panemiseks