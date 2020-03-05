
"""
I thought it would be a good idea to seperate the classes by file for better readability
"""

class Cell:
#-----------------------------------------------------------------------------------
#core atributes
  infectionStatus = 0 # once a Cell is not alive, it should destruct, and return false
  Column = 0 # tracking positiong of the Cell
  Row = 0
  age = 0
  timeHealthy = 0
  timeVirus = 0
  gameBoard = []
#-----------------------------------------------------------------------------------
#constructors
  def __init__ (self, age, infectionStat,row, column, timehealthy, timevirus, board):
    self.gameBoard = board
    self.age = age
    self.infectionStatus = infectionStat # 1 or 0
    self.Column = column
    self.Row = row
    self.timeHealthy = timehealthy
    self.timeVirus = timevirus

#------------------------------------------------------------------------------------
#get functions for core attributes
  def getColumn(self):
    return self.Column
  def getRow(self):
    return self.Row
  def getAge(self):
    return self.age
  def get_timeHealthy(self):
    return timeHealthy
  def get_timeVirus(self):
    return timeVirus
  def getInfectionStatus(self):
    return infectionStatus
  def isVulnerable(self):
    return int((self.age >= 74) or (self.age <=4))
  def isOld(self):
    return int(self.age >= 74)

# -----------------------------------------------------------------------------------------
#set functions

  def setPos(self,x,y): # setting x,y coords
    self.Column = x
    self.Row = y

  def movePos(self,x,y): # this function is tied to move function
    self.Column += x # adding movement to horiz
    self.Row += y # adding movement to vert
  
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

  def move(self):
    seed(8) # seeding random nujmber
    x = randint(-1,1) # getting horiz value to add to new pos
    y = randint(-1,1) # getting vert value to add to new pos
    self.movePos(x,y)

  # def deathRate(self):
  #   oldAge = (self.isOld()*0.10)
  #   print("Prob due to oldAge is ", oldAge)
  #   mean = 70 # 70 days for top virus death
  #   stdev = 2 # 2 days for standard deviation
  #   probVirusDeath = scipy.stats.norm(500,100).cdf(self.timeVirus)-0.01 # doens't work :()
  #   probVirusDeath = (probVirusDeath - 0.1)/(0.5-0.1)
  #   print("Prob due to virus is ", probVirusDeath)
  #   vulnerable = (self.isVulnerable()*0.2)
  #   print("Prob due to vulnerability is ", vulnerable)
  #   return (oldAge + probVirusDeath + vulnerable)
  
