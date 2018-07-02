import filterpy
import pygame, sys
import numpy as np
from enum import Enum, unique

pygame.init()
size = width, height = 500, 500
black = 0, 0, 0
red = 255,0,0
white = 255,255,255
colors = [white, black, red]
screen = pygame.display.set_mode(size)

N = 5 # grid size
SIZE = 100
@unique
class HEADINGS(Enum):
    N = (-1,0)
    E = (0,1)
    S = (1,0)
    W = (0,-1)

    def turn(self, c):
        if c == 'L':
            d = -1
        elif c == 'R':
            d = 1
        else:
            d = 0
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + d
        if index >= len(members):
            index = 0
        return members[index]


def move(board, loc, orientation):
    temp = (loc + orientation.value) % N
    if board[temp[0], temp[1]] == -1:
        return loc
    board[loc[0],loc[1]] = 0
    loc += orientation.value
    loc = loc % N
    board[loc[0], loc[1]] = 1
    return loc


def display(screen):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            screen.fill(colors[int(board[i,j])], rect=grid[i,j])
    pygame.display.flip()


board = np.zeros((N, N))
orientation = HEADINGS.N
loc = np.array([0,0])
board[loc[0], loc[1]] = 1
board[1,1:4] = -1
grid = []
for i in range(N):
        grid.append([pygame.Rect(SIZE*j, SIZE*i, SIZE, SIZE) for j in range(N)])
grid = np.array(grid)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        loc = move(board, loc, orientation)
    if pressed[pygame.K_d]:
        orientation = orientation.turn("R")
    if pressed[pygame.K_a]:
        orientation = orientation.turn("L")
    display(screen)
    pygame.time.wait(100)