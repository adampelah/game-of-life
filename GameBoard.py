import numpy as np
import matplotlib.pyplot as plt
import random as rd
from Cell import Cell
import info


class Board:

    # Core attributes
    size = 100
    grid = np.zeros((size, size))
    cell_list = []
    infectedCount = 0
    population = 0
    
    def __init__(self, inSize):  # creating parameter for user
        
        self.size = inSize
        self.grid = np.zeros((inSize, inSize))
        cell_list = []

    def relativePopulation(self, state): # this function grabs population from census information
        return int(info.getPopulationSize(state))
    
    def getPercentInfected(self, state):
        return float(info.getTotalCases(state)/info.getPopulation(state))

    def createPopulation (self, state):  # creates a population based on parameters and board

        self.population = self.relativePopulation(state)
        self.infectedCount = int(self.population * self.getPercentInfected(state))
        if(self.infectedCount < 50):
            self.infectedCount = 75
       
        randomCoord = [0,0]
        randomCoord[0] = (rd.randint(1, self.size - 1))  # location x
        randomCoord[1] = (rd.randint(1, self.size - 1))  # location y

        for x in range(0, self.population):

            infectionStatus = 1
            if x < self.infectedCount: # this condition creates number of infected sells specified by parameters
                infectionStatus = 2

            # get random coordinates for cell
            while (self.grid[randomCoord[0], randomCoord[1]] != 0):
                randomCoord[0] = rd.randint(0, self.size - 1)  # location x
                randomCoord[1] = rd.randint(0, self.size -1)  # location y

            # generate random cell
            new_cell = Cell(rd.randint(1, 80),  # age
                            infectionStatus,  # infection stat
                            randomCoord[0],  # location x
                            randomCoord[1],  # location y
                            rd.randint(0, 255),  # time
                            self) 

            self.cell_list.append( new_cell ) # add cell to dictionary
            self.grid[new_cell.Row, new_cell.Column] = new_cell.infectionStatus  # add cell status to grid
        
    def update_grid(self):
        for index,cell in enumerate(self.cell_list):
            if(cell.time % 60 == 0):
                if(cell.deathRate()):
                    self.cell_list.pop(index)            
            cell.move()


    def show(self):
        while len(self.cell_list) > self.population/4:  # Visualize the grid
            plt.imshow(self.grid)
            plt.title("Population: " + str(len(self.cell_list)))
            plt.xlabel("starting infection count = " + str(self.infectedCount))
            self.update_grid()
            plt.pause(0.0000005)
            plt.clf()
