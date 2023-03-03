import pygame


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
light_blue = (138, 235, 255)

y = 480
x = 640
screen = pygame.display.set_mode((x , y))
screen.fill(light_blue)
pygame.display.set_caption("Ping-Pong, Ott-Saamuel Oja")



pygame.display.update()
running=True
# Hakkab tsükkel. Selle abil saab panna X ekraani kinni.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
