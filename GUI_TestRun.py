import pygame
import random

from moves import*

pygame.init()

WIDTH, HEIGHT = 630,630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE=(255, 255, 255)
GRAY = (170,170,170)
D_GRAY = (85,85,85)

PURPLE = (130,0,255)
PINK = (230,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
L_BLUE = (0,130,130)
D_BLUE = (0,25,255)
ORANGE = (255,150,0)
SKY_BLUE = (0,255,255)
D_ORANGE = (255,120,0)
L_RED = (255,140,140)
RED = (255,0,0)
 


box_color = [WHITE, PURPLE, PINK, YELLOW, GREEN, L_BLUE, D_BLUE, ORANGE, SKY_BLUE, D_ORANGE, L_RED, RED, RED]


WORD_FONT = pygame.font.SysFont('comicsans', 300)

pygame.display.set_caption("2048")


run = True


#initialize main grid
grid = {}
for i in range(4):
    grid[i] = []
    for j in range(4):
        grid[i].append(0)



#create 2 random 2s

temporary_x = random.randint(0,3)
temporary_y = random.randint(0,3)
grid[temporary_x][temporary_y]=2
while(grid[temporary_x][temporary_y]==2):
    temporary_x = random.randint(0,3)
    temporary_y = random.randint(0,3)
grid[temporary_x][temporary_y]=2





def draw():
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(WIN, box_color[lg(grid[i][j])], (5+150*i,5+150*j, 145, 145))
            output = WORD_FONT.render(f"{grid[i][j]}", 100, BLACK)
            output = pygame.transform.scale(output, (75,75))
            WIN.blit(output, (40+150*i,40+150*j))
            if(grid[i][j]==0):
                pygame.draw.rect(WIN, box_color[lg(grid[i][j])], (5+150*i,5+150*j, 145, 145))




print(grid)


while run:

    execute = False
    ok = False
    #time delay
    pygame.time.delay(10)


    for event in pygame.event.get():
        if (event.type==pygame.QUIT): run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                grid,ok = move_up(grid)

            if event.key == pygame.K_DOWN:
                grid,ok = move_down(grid)
            
            if event.key == pygame.K_LEFT:
                grid,ok = move_left(grid)

            if event.key == pygame.K_RIGHT:
                grid,ok = move_right(grid)
            
            WIN.fill(D_GRAY)
            draw()
            pygame.display.update()
            pygame.time.delay(10)
            #change the following to minimax
            if(ok==False):continue
            temporary_x = random.randint(0,3)
            temporary_y = random.randint(0,3)
            Full = True
            for i in range(4):
                for j in range(4):
                    if(grid[i][j] == 0): Full = False
            if(Full==False):
                while(grid[temporary_x][temporary_y]!=0):
                    temporary_x = random.randint(0,3)
                    temporary_y = random.randint(0,3)
                grid[temporary_x][temporary_y]=2




    WIN.fill(D_GRAY)
    draw()
    pygame.display.update()

    





pygame.quit()