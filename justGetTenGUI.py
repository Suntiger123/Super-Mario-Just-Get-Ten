import sys, pygame
from bases import *
from merge import *
from possible import *

pygame.init()

# Init vars
mapSize = 5
cellSize = 32
xPos = 289
yPos = 231
proba=(0.05,0.30,0.6)
firstSelection = False
size = width, height = 1088, 607
gameBoard = gameBoard(mapSize, proba)
display(gameBoard)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Mario Get Ten")

# Images loading
surface = pygame.image.load("images/surface-5x5.png")
numOne = pygame.image.load("images/1.png")
numTwo = pygame.image.load("images/2.png")
numThree = pygame.image.load("images/3.png")
numFour = pygame.image.load("images/4.png")
numFive = pygame.image.load("images/5.png")
numSix = pygame.image.load("images/6.png")
numSeven = pygame.image.load("images/7.png")
numEight = pygame.image.load("images/8.png")
numNine = pygame.image.load("images/9.png")
selectedCellEffect = pygame.image.load("images/selected.png")

# Images object
cells = {
    1: numOne,
    2: numTwo,
    3: numThree,
    4: numFour,
    5: numFive,
    6: numSix,
    7: numSeven,
    8: numEight,
    9: numNine
}

# Functions
def drawGrid():
    for col in range(mapSize):
        for row in range(mapSize):
            # Prepare to display correct numeric image according gameBoard cell value in the correct position
            surface.blit(cells[gameBoard[col][row]], (yPos + row*cellSize, xPos + col*cellSize, cellSize, cellSize))

# Startup draw
drawGrid()

# Main Loop
while 1:
    # Calculate mousePos based on gameBoard grid
    mouseX = (pygame.mouse.get_pos()[1] - xPos) // cellSize
    mouseY = (pygame.mouse.get_pos()[0] - yPos) // cellSize

    # Events loop
    for event in pygame.event.get():
        # Manage quit / closing window event
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        # Display mousePos on window title bar
        elif event.type == pygame.MOUSEMOTION:
            if mouseX >= 0 and mouseY >= 0:
                if mouseX < mapSize and mouseY < mapSize:
                    text = "mouseX: {0} - mouseY: {1}".format(mouseX, mouseY)
                    pygame.display.set_caption("Super Mario Get Ten - " + text)
                else:
                    pygame.display.set_caption("Super Mario Get Ten")
            else:
                pygame.display.set_caption("Super Mario Get Ten")

        # 
        if firstSelection == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseX >= 0 and mouseY >= 0:
                    if mouseX < mapSize and mouseY < mapSize:
                        if adjCells(mapSize, gameBoard, mouseX, mouseY):
                            firstSelection = True
                            myTuple = (mouseX, mouseY)
                            tupleList = [myTuple]
                            propagation(mapSize, gameBoard, myTuple, tupleList)
                            for item in range(len(tupleList)):
                                currentPos = tupleList[item]
                                surface.blit(selectedCellEffect, (yPos + currentPos[1]*cellSize, xPos + currentPos[0]*cellSize, cellSize, cellSize))
                        else:
                            # play error sound, no adjacent cells
                            print('No Adj Cells')  
        elif firstSelection == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseX >= 0 and mouseY >= 0:
                    if mouseX < mapSize and mouseY < mapSize:
                        if adjCells(mapSize, gameBoard, mouseX, mouseY):
                            firstSelection= False
                            myTuple = (mouseX, mouseY)
                            tupleList = [myTuple]
                            propagation(mapSize, gameBoard, myTuple, tupleList)
                            modification(mapSize, gameBoard, tupleList)
                            gravity(mapSize, gameBoard, proba)
                            drawGrid()
                      

    screen.blit(surface, (0, 0))
    pygame.display.update()
