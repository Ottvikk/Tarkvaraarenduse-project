
import pygame
import random
import sys

# initsialiseerime pygame'i
pygame.init()

# ekraani mõõtmed
screen_width = 500
screen_height = 500
taust = pygame.image.load("grass.png")
taust = pygame.transform.scale(taust, [screen_width, screen_height])
# määratleme värvid RGB formaadis
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# loome ekraani
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game by Ott-Saamuel Oja")
high_score_file = open('high_score.txt', 'r')
high_score = int(high_score_file.read())
high_score_file.close()
Sound = pygame.mixer.Sound('apple_bite.ogg')
pygame.mixer.Sound.set_volume(Sound,1)

with open('high_score.txt', 'r') as file:
    high_score = int(file.read())

# snake'i alguskoordinaadid ja suund
x = screen_width // 2
y = screen_height // 2
direction = 'right'

# loome snake'i
snake = []
snake_length = 1
snake_block_size = 10
snake_speed = 10

# loome toidu
food_x = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0

# loome takistused
obstacles = []
obstacle_size = 20
num_obstacles = 0
max_obstacles = 5

# funktsioon teksti joonistamiseks ekraanile
def draw_text(text, font_size, color, x, y):
    font = pygame.font.SysFont(None, font_size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

# funktsioon snake'i joonistamiseks ekraanile
def draw_snake(snake_block_size, snake_list):
    for x,y in snake_list:
        pygame.draw.rect(screen, black, [x, y, snake_block_size, snake_block_size])

# snake'i liikumine
def move_snake(x, y, snake_list, direction):
    if direction == 'right':
        x += snake_speed
    elif direction == 'left':
        x -= snake_speed
    elif direction == 'up':
        y -= snake_speed
    elif direction == 'down':
        y += snake_speed

    # lisame uue snake'i bloki listi lõppu
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    # eemaldame vanima bloki, kui snake on liiga pikk
    if len(snake_list) > snake_length:
        del snake_list[0]

    return x, y, snake_list

# loome takistused juhuvalt ekraanile
def create_obstacle():
    global num_obstacles
    if num_obstacles < max_obstacles:
        obstacle_x = round(random.randrange(0, screen_width - obstacle_size) / 10.0) * 10.0
        obstacle_y = round(random.randrange(0, screen_height - obstacle_size) / 10.0) * 10.0
        obstacles.append([obstacle_x, obstacle_y])
        num_obstacles += 1

# mängu tsükkel
game_over = False
clock = pygame.time.Clock()
score = 0
level = 1

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'

    # taustavärv
    screen.blit(taust,(0,0))

    # joonistame snake'i
    snake_head = [x, y]
    snake_list = []
    snake_list.append(snake_head)
    draw_snake(snake_block_size, snake_list)

    # liigutame snake'i
    x, y, snake = move_snake(x, y, snake, direction)

    # joonistame toidu
    pygame.draw.rect(screen, red, [food_x, food_y, snake_block_size, snake_block_size])

    # kui snake sööb toidu
    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0
        snake_length += 1
        score += 5
        pygame.mixer.Sound.play(Sound)
        if score % 20 == 0:
            max_obstacles += 1
            level += 1

    if score > high_score:
        high_score = score
        with open('high_score.txt', 'w') as file:
            file.write(str(high_score))

    # loome takistusi
    create_obstacle()

    # joonistame takistused
    for obstacle in obstacles:
        pygame.draw.rect(screen, green, [obstacle[0], obstacle[1], obstacle_size, obstacle_size])

    # kui snake läheb takistusega kokku
    for obstacle in obstacles:
        if obstacle[0] == x and obstacle[1] == y:
            game_over = True

    # kui snake läheb ekraanist välja
    if x >= screen_width or x < 0 or y >= screen_height or y < 0:
        game_over = True

    # joonistame skoori ja leveli
    draw_text("High Score: " + str(high_score), 20, black, 250, 10)
    draw_text("Score: " + str(score), 20, black, 10, 10)
    draw_text("Level: " + str(level), 20, black, screen_width - 100, 10)

    # uuendame ekraani
    pygame.display.update()

    # määrame FPS'i
    clock.tick(20)

# lõpetame pygame'i
pygame.quit()