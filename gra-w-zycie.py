import pygame, sys
from pygame.locals import *
import random

#--zmienne globalne--#
FPS = 7

BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)
GREEN =    (0,255,0)

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

CELLWIDTH = WINDOWWIDTH / CELLSIZE # number of cells wide
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE # Number of cells high

#asserts that width and height are multiples of the cell size.
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # pionowe linie
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # poziome linie
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH, y))

# life cells -> green, dead cells -> white
def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE # array -> grid size
    x = x * CELLSIZE # array -> grid size
    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELLSIZE, CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, CELLSIZE, CELLSIZE))
    return None

# tworzy slownik z komorkami
# wszystkie martwe (0)
def blankGrid():
    gridDict = {}
    for y in range(CELLHEIGHT):
        for x in range(CELLWIDTH):
            gridDict[x,y] = 0 # zeruje
    return gridDict

# random: 0 || 1 to all cells
def startingGridRandom(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

def drawGlider(lifeDict, x):
  lifeDict[x+1, x] = 1
  lifeDict[x+2, x+1] = 1
  lifeDict[x, x+2] = 1
  lifeDict[x+1, x+2] = 1
  lifeDict[x+2, x+2] = 1
  return lifeDict

def drawOscilator(lifeDict, x, size):
  """lifeDict[x, x] = 1
  lifeDict[x, x+1] = 1
  lifeDict[x, x+2] = 1"""
  
  for i in range(size):
    lifeDict[x, x+i] = 1
  return lifeDict

# liczba sasiadow
def getNeighbours(item,lifeDict):
    neighbours = 0
    for x in range (-1,2):
        for y in range (-1,2):
            checkCell = (item[0]+x,item[1]+y)
            if checkCell[0] < CELLWIDTH  and checkCell[0] >=0:
                if checkCell [1] < CELLHEIGHT and checkCell[1]>= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0: # negate the central cell
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

# next tick
def tick(lifeDict):
    newTick = {} # stan w nowym ticku
    for item in lifeDict:
        # wez liczbe sasiadow
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1: # dla obecnie zywych
            if numberNeighbours < 2: # samotnosc : (
                newTick[item] = 0
            elif numberNeighbours > 3: # przeludnienie
                newTick[item] = 0
            else:
                newTick[item] = 1 # pozostan zywy
        elif lifeDict[item] == 0: # dla obecnie martwych
            if numberNeighbours == 3: # narodziny
                newTick[item] = 1
            else:
                newTick[item] = 0 # byles martwy, pozostan martwy
    return newTick



def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Game of Life')

    DISPLAYSURF.fill(WHITE)

    lifeDict = blankGrid()

    #lifeDict = startingGridRandom(lifeDict) # RANDOM
    #lifeDict = drawGlider(lifeDict, 20) # GLIDER
    lifeDict = drawOscilator(lifeDict, 20, 60) # OSCILATOR, 3 parameter == size
    
    #Colours the live cells, blanks the dead
    for item in lifeDict:
        colourGrid(item, lifeDict)

    drawGrid()
    pygame.display.update()
    
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #runs a tick
        lifeDict = tick(lifeDict)

        # Colours the live cells, blanks the dead
        for item in lifeDict:
            colourGrid(item, lifeDict)

        drawGrid()
        pygame.display.update()    
        FPSCLOCK.tick(FPS)
        
if __name__=='__main__':
    main()