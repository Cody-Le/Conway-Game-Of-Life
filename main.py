import copy

import pygame
import numpy as np
import time

#Any live cell with two or three live neighbours survives.
#Any dead cell with three live neighbours becomes a live cell.
#All other live cells die in the next generation. Similarly, all other dead cells stay dead.

#---------------------- variable intialization
height, width = [30,30]
#The varaible that dictate the behavior of the games
underPopRate = 2
highPopRate = 3
minimumSpawnRate = 3

#---------------------- function def
#Function implement the rule of the game
def rule(CellList, WorldSpace, width, height):
    newSpace = copy.deepcopy(WorldSpace)
    newCells = copy.deepcopy(CellList)
    for x in range(1, width - 1):
        for y in range(1,height - 1):
            SCell = WorldSpace[x,y+1] + WorldSpace[x+1,y+1] + WorldSpace[x+1,y] + WorldSpace[x+1, y-1]\
                    + WorldSpace[x, y - 1] + WorldSpace[x - 1, y -1] + WorldSpace[x-1, y] + WorldSpace[x-1, y + 1]





            if WorldSpace[x, y] == 1:

                if (SCell < underPopRate or SCell > highPopRate):

                    newCells = newCells[np.where((newCells != (x,y)).any(axis = 1))]
                    #ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
                    newSpace[x,y] = 0
                    pass

            else:
                if SCell == minimumSpawnRate:


                    newSpace[x, y] = 1
                    newCells = np.concatenate((newCells, [[x,y]]), axis = 0)

                    pass


    return newSpace, newCells #Function to i

#Function to render the position to image
def makeImages(CellList, dimSize, scale):
    picMa = np.zeros((dimSize[0] * scale + 1, dimSize[1] * scale + 1))
    a = np.arange(1, scale + 1)
    replMa = np.hstack((np.repeat(a, scale)[:,np.newaxis], np.tile(a, scale)[:,np.newaxis]))
    for index in CellList:

        replIndex = (index - 1) * scale + replMa
        picMa[replIndex[:,0], replIndex[:,1]]  = 1

    surface = pygame.surfarray.make_surface(picMa * 250)


    return surface


#Function to toggle the cell on or off
def mouseInput(mLoc, CellList, WorldSpace, dim, scale):
    index = ((mLoc - np.mod(mLoc,scale))/scale + 1).astype(int)
    if WorldSpace[index[0], index[1]] == 1:
        CellList = CellList[np.where((CellList != (index[0], index[1])).any(axis=1))]
        WorldSpace[index[0], index[1]] = 0
    else:
        WorldSpace[index[0], index[1]] = 1
        CellList = np.concatenate((CellList, [[index[0], index[1]]]), axis=0)
    return makeImages(CellList, dim, scale), CellList, WorldSpace


#worldSpace = np.zeros((height, width))

worldSpace = np.zeros((width, height))

ACell = np.array([
    [5,5],
    [6,6],
    [6,7],
    [5,7],
    [4,7]
])




#connect ACell to worldSpace
worldSpace[ACell[:,0], ACell[:,1]] = 1

#----------------------------------------------------------------- yeh

print("""
Welcome to python version of Conways game of life
The Rules of the game are:
. Any live cell with 2 (underPopRate) or 3 (highPopRate) live neighbours survives.
. Any dead cell with 3 (minimumSpawnRate) live neighbours becomes a live cell.
. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

Edit the variables to change the looks and behavior of the game
THe default delay time is 0.18s, for faster game, reduce the number

[Space] to play/pause the space
[Tab] to clear the game, this only work if paused
Left Click to anywhere to kill or spawn a cell

Have Fun!!! 
""")





pygame.init()

pygame.display.set_caption('GoL')
window_surface = pygame.display.set_mode((800, 800))

background = pygame.Surface((800, 800))
background.fill(pygame.Color('#000000'))

is_running = True
is_pausing = True
scale = int(800/max(width, height))


img = makeImages(ACell, (width + 1, height + 1), scale)
window_surface.blit(background, (0, 0))
worldSpace, ACell = rule(ACell, worldSpace, width, height)
window_surface.blit(img, (0, 0))



while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_pausing = not (is_pausing)
            if is_pausing:
                if event.key == pygame.K_TAB:
                    ACell = np.array([[0,0]])
                    worldSpace[:] = 0
                    img = makeImages(ACell, (width + 1, height + 1), scale )
                    window_surface.blit(img, (0,0))
        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            img, ACell, worldSpace = mouseInput(np.array(pos), ACell, worldSpace, (width + 1, height + 1), scale)
            window_surface.blit(img, (0,0))


    if not is_pausing:
        time.sleep(0.18)
        img = makeImages(ACell, (width + 1, height + 1), scale)
        window_surface.blit(background, (0, 0))
        worldSpace, ACell = rule(ACell, worldSpace, width, height)
        window_surface.blit(img, (0, 0))



    pygame.display.update()



