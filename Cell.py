import sys

sys.path.append("..")
import time
import random
from scipy import signal
import numpy
import time as tm


kernel = numpy.ones((3, 3), dtype=numpy.int8)
kernel[1, 1] = 0

class Cell:
    # -----------------------------------------------------------------------------------
    # core attributes
    infectionStatus = 0  # once a Cell is not alive, it should destruct, and return false
    Column = 0  # tracking position of the Cell
    Row = 0
    age = 0
    timeHealthy = 0
    timeVirus = 0

    # -----------------------------------------------------------------------------------
    # constructors
    def __init__(self, age, infectionStat, row, column, timevirus, board):

        self.age = age
        self.infectionStatus = infectionStat  # 1 or 0
        self.Column = column
        self.Row = row
        self.time = 0
        self.timeVirus = timevirus
        self.gameBoard = board

    # ------------------------------------------------------------------------------------
    # get functions for core attributes
    def getColumn(self):
        return self.Column

    def getRow(self):
        return self.Row

    def getAge(self):
        return self.age

    def get_timeHealthy(self):
        return self.timeHealthy

    def get_timeVirus(self):
        return self.timeVirus

    def getInfectionStatus(self):
        return self.infectionStatus

    def isVulnerable(self):
        return int((self.age >= 74) or (self.age <= 4))

    def isOld(self):
        return int(self.age >= 74)

    def hasVirus(self):
        return int(self.infectionStatus == 2 )

    # -----------------------------------------------------------------------------------------
    # set functions

    def addYear(self):  # checks if year has happened
        if (self.timeHealthy + self.timeVirus % 365 == 0):  ## if a year has passed
            self.age += 1  # adding one year to the age

    def set_timeVirus(self, num):
        self.timeVirus = num

    def set_timeHealthy(self, num):
        self.timeHealthy = num

    def setInfectionStatus(self, stat):
        self.infectionStatus = stat

    # move functions---------------------------------------------------------------------------------
    def setPos(self,x,y): # setting x,y coords
        # this function checks the bounds of the board
        if(x > self.gameBoard.size -1 or y > self.gameBoard.size-1 or x < 0 or y < 0):
            return
        self.gameBoard.grid[self.Row][self.Column] = 0
        self.Column = y
        self.Row = x
        self.gameBoard.grid[x, y] = self.infectionStatus

    def returnKernel(self, miniboard):

        for x in range(0, 3):
            for y in range(0, 3):
                miniboard[x][y] = self.gameBoard.grid[self.Row-1+x% self.gameBoard.size-1][self.Row-1+y% self.gameBoard.size-1]
        miniboard[1][1] = self.infectionStatus

    def move(self):
        newrow = self.Row
        newcol = self.Column
        if (self.infectionStatus == 1):  # move for healthy cells, finding the least crowded space
            miniboard = numpy.ones((3, 3), dtype=int)
            self.returnKernel(miniboard)
            neighbour = signal.convolve(miniboard, kernel, mode='same')  # count neighbors
            neighbour[1][1] = 999
            j = numpy.argwhere(neighbour == numpy.min(neighbour))
            x = random.randrange(0, len(j))
            minindex = j[x]
            newrow = self.Row + minindex[0]-1
            newcol = self.Column + minindex[1]-1


        elif (self.infectionStatus == 2):
            # SET RANDOM POSITION FOR INFECTED CELLS
            newrow = self.Row + (random.randint(-1, 1))
            newcol = self.Column + (random.randint(-1, 1))

        self.collision()
        self.setPos(newrow, newcol)
        self.time += 1

    def collision(self):
        if(self.infectionStatus == 1 and self.gameBoard.grid[self.Row, self.Column] == 2):
            if (random.randint(0,2) == 2):
                self.infectionStatus = 2
                self.gameBoard.infectedCount += 1  # updating infected count of population

    def deathRate(self):  # All encopassing death rate function for cells.
        virus = self.hasVirus()
        vulnerable = self.isVulnerable()
        total = (vulnerable + virus)
        if random.randint(0, 10) <= total:
            self.gameBoard.infectedCount -= 1
            self.gameBoard.grid[self.Row, self.Column] = 0
            return 1
        return 0