import pygame
screen = pygame.display.set_mode((640, 480))



running=True
#Tsükkel hakkab
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()