import sys

sys.path.append("..")
import random
from scipy import signal
import numpy


class Cell:
    # -----------------------------------------------------------------------------------
    # core atributes
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
        return self.infectionStatus == 2

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
    def setPos(self, x, y):  # setting x,y coords
        # this function checks the bounds of the board
        if (x >= self.gameBoard.size - 1):
            return
        if (y >= self.gameBoard.size - 1):
            return
        if (x <= 1):
            return
        if (y <= 1):
            return

        self.Column = y
        self.Row = x

    def returnKernel(self):
      miniboard = numpy.ones((3, 3), dtype=int)
      miniboard[0][0] = self.gameBoard.grid[(self.Row - 1) % self.gameBoard.size][
        (self.Column - 1) % self.gameBoard.size]
      miniboard[0][1] = self.gameBoard.grid[(self.Row - 1) % self.gameBoard.size][(self.Column)]
      miniboard[0][2] = self.gameBoard.grid[(self.Row - 1) % self.gameBoard.size][
        (self.Column + 1) % self.gameBoard.size]
      miniboard[1][0] = self.gameBoard.grid[(self.Row)][(self.Column - 1) % self.gameBoard.size]
      miniboard[1][1] = self.infectionStatus
      miniboard[1][2] = self.gameBoard.grid[(self.Row)][(self.Column + 1) % self.gameBoard.size]
      miniboard[2][0] = self.gameBoard.grid[(self.Row + 1) % self.gameBoard.size][
        (self.Column - 1) % self.gameBoard.size]
      miniboard[2][1] = self.gameBoard.grid[(self.Row + 1) % self.gameBoard.size][(self.Column)]
      miniboard[2][2] = self.gameBoard.grid[(self.Row + 1) % self.gameBoard.size][
        (self.Column + 1) % self.gameBoard.size]
      return miniboard


    def getPosInGrid(self, x, y):
      return self.Row + x, self.Column + y

    def move(self):
      newrow = self.Row
      newcol = self.Column
      if (self.infectionStatus == 1):  # move for healthy cells, finding the least crowded space
        kernel = numpy.ones((3, 3), dtype=numpy.int8)
        kernel[1, 1] = 0
        miniboard = self.returnKernel()
        neighbour = signal.convolve(miniboard, kernel, mode='same')  # count neighbors
        neighbour[1][1] = 999
        j = numpy.argwhere(neighbour == numpy.min(neighbour))
        x = random.randrange(0, len(j))
        minindex = j[x]
        newrow, newcol = self.getPosInGrid(minindex[0] - 1, minindex[1]- 1)
        #print("Mini section of board\n", miniboard, "Neighbour count for section\n", neighbour, minindex, newrow, newcol)
        # if(self.gameBoard.grid[newrow][newcol]!=0):
        # IF POSITION OCCUPIED, perform collision
        # self.collision()

      elif(self.infectionStatus==2):
        #SET RANDOM POSITION FOR INFECTED CELLS
       newrow = self.Row + (random.randint(-1, 1))
       newcol = self.Column + (random.randint(-1, 1))

        # IF POSITION OCCUPIED, perform collision
        # if(self.gameBoard.grid[newrow][newcol]!=0):
        # self.collision()

      self.setPos(newrow, newcol)

    def collision(self):  # Collision function with other cells
        if (self.infectionStatus == 1):
            x = random.randint(0, 2)
            if (x == 2):
                self.infectionStatus = 2  # set to infected
                self.gameBoard.infectedCount += 1  # updating infected count of population

    def deathRate(self):  # All encompassing death rate function for cells.
        virus = self.hasVirus() * 0.00005
        vulnerable = (self.isVulnerable() * 0.00005)
        daily = 0.00005
        total = (daily + vulnerable + virus)
        if random.random() <= total:
            self.gameBoard.infectedCount -= 1
            return 1
        return 0