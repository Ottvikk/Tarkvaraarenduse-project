
import pygame, random, sys

red = [255, 0, 0]

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Death rally")
clock = pygame.time.Clock()
score = 0

bg_rally = pygame.image.load("img/bg_rally.jpg")
f1_red = pygame.image.load("img/f1_red.png")
f1_blue = pygame.image.load("img/f1_blue.png")
blue1 = f1_blue
blue2 = f1_blue

Bspeed = 5

Blue1X, Blue1Y = random.randint(130,460), random.randint(0,100)
Blue2X, Blue2Y = random.randint(130,460), random.randint(0,100)
RedX, RedY = 300, 370

gameover = False
while not gameover:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(bg_rally, [0,0])
    screen.blit(blue1, (Blue1X, Blue1Y))
    screen.blit(blue2, (Blue2X, Blue2Y))
    Blue1Y += Bspeed - 0.5
    Blue2Y += Bspeed
    screen.blit(f1_red,(RedX, RedY))

    screen.blit(pygame.font.Font(None, 28).render(f"Score: {score}", True, red,) (10,20))


    pygame.display.update()

pygame.quit()
