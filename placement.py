#pygame
import os
import pygame
import random

pygame.font.init()
Shape = [['..0..',
      '.000.',
      '00000',
      '.....',
      '.....'],
     ['..0..',
      '..00.',
      '..000',
      '..00.',
      '..0..'],
      ['.....',
      '.....',
      '00000',
      '.000.',
      '..0..'],
      ['..0..',
       '.00..',
       '000..',
       '.00..',
       '..0..']]
Line = [['..00.',
      '..00.',
      '..00.',
      '..00.',
      '..00.'],
     ['.....',
      '.....',
      '00000',
      '00000',
      '.....']]
shapes = [Shape,Line]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[random.randint(0,len(shape_colors)-1)]
        self.rotation = 0

def create_grid(locked_pos={}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if((j, i)in locked_pos):
                con = locked_pos[(j,i)]
                grid[i][j] = con
    return grid

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if(column=='0'):
                positions.append((shape.x + j, shape.y + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions

def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if(grid[i][j]==(0,0,0))] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if(not pos in accepted_pos):
            if(len(pos)>=2)and(pos[1]>=0):
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if(y<1):
            return True
    return False

def get_shape():
    return Piece(5, 0, random.choice(shapes))

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (225 - (label.get_width()/2), 400 - label.get_height()/2))

def draw_grid(surface, grid):
    sx = 250
    sy = 100
    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i*30), (sx+300, sy+ i*30))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*30, sy),(sx + j*30, sy + 600))

def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if(not(0,0,0)in row):
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j,i)]
                except:
                    continue
    if(inc>=1):
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if(y<ind):
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    return inc

def update_score(nscore):
    score = max_score()
    
def max_score():
    score='0'
    return score

def draw_window(surface, grid, score=0, last_score = 0):
    surface.fill((0, 0, 0))
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (225 - (label.get_width() / 2), 30))
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255,255,255))
    sx = 600
    sy = 300
    surface.blit(label, (sx + 20, sy + 160))
    label = font.render('High Score: ' + str(last_score), 1, (255,255,255))
    sx = 50
    sy = 300
    surface.blit(label, (sx + 20, sy + 160))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (250 + j*30, 100 + i*30, 30, 30), 0)
    pygame.draw.rect(surface, (255, 0, 0), (250, 100, 300, 600), 5)
    draw_grid(surface, grid)

def main(win):
    last_score = max_score()
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0
    while(run):
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        if(level_time/1000>=4):
            level_time = 0
            if(level_time > 0.12):
                level_time-=0.005
        if(fall_time/1000>fall_speed):
            fall_time = 0
            current_piece.y += 1
            if(not valid_space(current_piece, grid))and(current_piece.y>=1):
                current_piece.y -= 1
                change_piece = True
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
                pygame.display.quit()
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    current_piece.x -= 1
                    if(not valid_space(current_piece, grid)):
                        current_piece.x += 1
                elif(event.key == pygame.K_RIGHT):
                    current_piece.x += 1
                    if(not valid_space(current_piece, grid)):
                        current_piece.x -= 1
                elif(event.key == pygame.K_DOWN):
                    current_piece.y += 1
                    if(not valid_space(current_piece, grid)):
                        current_piece.y -= 1
                else:
                    current_piece.rotation += 1
                    if(not valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if(y>=0):
                grid[y][x] = current_piece.color
        if(change_piece):
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10
        draw_window(win, grid, score, last_score)
        pygame.display.update()
        if(check_lost(locked_positions)):
            draw_text_middle(win, 'YOU LOST!', 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)

def main_menu(win):
    run = True
    while(run):
        win.fill((0,0,0))
        draw_text_middle(win,'Press Any Key To Play', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            elif(event.type == pygame.KEYDOWN):
                main(win)
    pygame.display.quit()

win = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Placement')
main_menu(win)
