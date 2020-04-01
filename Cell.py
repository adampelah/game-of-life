import sys
sys.path.append("..")
import random


class Cell:
#-----------------------------------------------------------------------------------
#core atributes
  infectionStatus = 0 # once a Cell is not alive, it should destruct, and return false
  Column = 0 # tracking positiong of the Cell
  Row = 0
  age = 0
  timeHealthy = 0
  timeVirus = 0
 
#-----------------------------------------------------------------------------------
#constructors
  def __init__ (self, age, infectionStat,row, column, timehealthy, timevirus, board):
   
    self.age = age
    self.infectionStatus = infectionStat # 1 or 0
    self.Column = column
    self.Row = row
    self.timeHealthy = timehealthy
    self.timeVirus = timevirus
    self.gameBoard = board

#------------------------------------------------------------------------------------
#get functions for core attributes
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
    return int((self.age >= 74) or (self.age <=4))
  def isOld(self):
    return int(self.age >= 74)
  def hasVirus(self):
    return self.infectionStatus == 2

# -----------------------------------------------------------------------------------------
#set functions

  def addYear(self): # checks if year has happened
    if(self.timeHealthy + self.timeVirues %365 == 0): ## if a year has passed
      self.age+=1 # adding one year to the age

  def set_timeVirus(self,num):
    self.timeVirus = num
  
  def set_timeHealthy(self, num):
    self.timeHealthy = num

  def setInfectionStatus(self, stat):
    self.infectionStatus = stat

# move functions---------------------------------------------------------------------------------
  def setPos(self,x,y): # setting x,y coords
                        # this function checks the bounds of the board
    if(x >= self.gameBoard.size -1):
      return
    if (y >= self.gameBoard.size - 1):
      return
    if ( x <= 1):
      return
    if (y <= 1):
      return

    self.Column = y
    self.Row = x

  def move(self, cellDict):

    x = self.Row + (random.randint(-1,1))
    y = self.Column + (random.randint(-1,1))
    
    while(self.gameBoard.grid[x,y] != 0):
      if cellDict[x,y].infectionStatus == 2:
        self.collision()

      x = self.Row + (random.randint(-1,1))
      y = self.Column + (random.randint(-1,1))

    self.setPos(x, y)


  def collision(self):
    if(self.infectionStatus == 1):
      x = random.randint(0,2)
      if (x == 2):
        self.infectionStatus = 2
        self.gameBoard.infectedCount += 1 # updating infected count of population

 

  def deathRate(self):
    virus = self.hasVirus()*0.005
    vulnerable = (self.isVulnerable()*0.005)
    daily = 0.005
    total = (daily + vulnerable + virus)
    if random.random() <= total:
      self.infectionStatus = 0

