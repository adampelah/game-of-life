import numpy as np
import matplotlib.pyplot as plt
import random as rd
from Cell import Cell
from info import getTotalCases, getTotalDeaths, getDeathRate, getPopulation

class Board:

    # Core attributes
    size = 100
    grid = np.zeros((size, size))
    cell_dict = {}
    infectedCount = 0
    population = 0
    
    def __init__(self, inSize):  # creating parameter for user
        
        self.size = inSize
        self.grid = np.zeros((inSize, inSize))
        cell_dict = {}

    def createPopulation (self, population, infected):  # creates a population based on parameters and board

        self.population = population + 1
        self.infectedCount = infected
        randomCoord = [0,0]
        randomCoord[0] = (rd.randint(1, self.size - 1))  # location x
        randomCoord[1] = (rd.randint(1, self.size - 1))  # location y

        for x in range(0, self.population -1):

            infectionStatus = 1
            if x < infected: # this condition creates number of infected sells specified by parameters
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

            self.cell_dict[new_cell.Row, new_cell.Column] = new_cell  # add cell to dictionary
            self.grid[new_cell.Row, new_cell.Column] = new_cell.infectionStatus  # add cell status to grid
        
    def update_grid(self):
        for x in range(0, self.size-1):
            for y in range(0, self.size-1):
                if (x, y) in self.cell_dict:
                    popped_cell = self.cell_dict.pop((x, y))  # get cell from 'grid' (accessed via dictionary)
                    self.grid[x][y] = 0  # set grid cell to 0
                    popped_cell.move()  # call move on cell

                    if(popped_cell.time % 10 != 0):  # Every 10 moves, no deaths
                        self.cell_dict[popped_cell.Row, popped_cell.Column] = popped_cell
                        self.grid[popped_cell.Row][popped_cell.Column] = popped_cell.infectionStatus
                    else:
                        #if(popped_cell.deathRate() == 0):  # Otherwise, call for death
                            self.cell_dict[popped_cell.Row, popped_cell.Column] = popped_cell
                            self.grid[popped_cell.Row][popped_cell.Column] = popped_cell.infectionStatus


    def show(self):
        while len(self.cell_dict) != 20:  # Visualize the grid
            plt.imshow(self.grid)
            plt.title("Population: " + str(len(self.cell_dict)))
            plt.xlabel("starting infection count = " + str(self.infectedCount))
            self.update_grid()
            plt.pause(0.0000005)
            plt.clf()
