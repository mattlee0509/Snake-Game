import pygame
import sys
import random
from sys import exit
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction= Vector2(-1,0)
    def draw_snake(self):
        for block in self.body:
            block_rect=pygame.Rect(int(block.x*cell_size),int(block.y*cell_size),cell_size,cell_size)
            pygame.draw.rect(screen, (0,0,0), block_rect)
    def move_snake(self):
        body_copy= self.body[:-1]
        body_copy.insert(0, body_copy[0]+ self.direction)
        self.body= body_copy[:]
    def add_block(self):
        body_copy= self.body[:]
        body_copy.insert(0, body_copy[0]+ self.direction)
        self.body= body_copy[:]
        
        

class FRUIT:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos= Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect= pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, ('Red'), fruit_rect)
    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos= Vector2(self.x,self.y)
class MAIN:
    def __init__(self):
        self.snake= SNAKE()
        self.fruit= FRUIT()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos== self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            
        
        if self.snake.body[0] in self.snake.body[2:]or self.snake.body[0].x<0 or self.snake.body[0].y<0 or self.snake.body[0].x>cell_size*cell_number or self.snake.body[0].y>cell_size*cell_number:
            pygame.quit()
            sys.exit()
            
            

            
            
        

pygame.init()
cell_size= 40
cell_number=20


pygame.display.set_caption('Snake game')

clock= pygame.time.Clock()

test_surface= pygame.Surface((cell_size,cell_size))
screen=pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))

run= True
z=0

SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

main_game= MAIN()
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and main_game.snake.direction!=Vector2(0,1):
                main_game.snake.direction=Vector2(0,-1)
            elif event.key==pygame.K_DOWN and main_game.snake.direction!=Vector2(0,-1):
                main_game.snake.direction=Vector2(0,1)
            elif event.key==pygame.K_LEFT and main_game.snake.direction!=Vector2(1,0):
                main_game.snake.direction=Vector2(-1,0)
            elif event.key==pygame.K_RIGHT and main_game.snake.direction!=Vector2(-1,0):
                main_game.snake.direction=Vector2(1,0)
        
    
        
    screen.fill('Yellow')
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
