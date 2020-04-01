import numpy as np
import matplotlib.pyplot as plt
import random as rd
from Cell import Cell


class Board:

    # Core attributes
    size = 100
    grid = np.zeros((size, size))
    cell_dict = {}
    
    def __init__(self):
        self.board = np.matrix('0 0 0; 0 0 0; 0 0 0')
        self.store_y = 0
        self.store_x = 0

    def setUpGrid(self):
        for x in range(0, 99):
            for y in range(0, 99):
                if (x, y) in self.cell_dict:
                    self.grid[x][y] = self.cell_dict[x, y].infectionStatus  # Fill grid spot

    def update_grid(self):
        for x in range(0, 99):
            for y in range(0, 99):
                if (x, y) in self.cell_dict:
                    popped_cell = self.cell_dict.pop((x, y))
                    self.grid[x][y] = 0
                    popped_cell.move()  # call move on cell
                    self.cell_dict[popped_cell.Row, popped_cell.Column] = popped_cell
                    self.grid[popped_cell.Row][popped_cell.Column] = popped_cell.infectionStatus

    def fill_dict(self):
        infectedCount = 0
        healthyCount = 0
        randomCoord = []
        randomCoord.append(rd.randint(0, 99))  # location x
        randomCoord.append(rd.randint(0, 99))  # location y

        for x in range(0, 200):

            while (self.grid[randomCoord[0], randomCoord[1]] != 0):
                randomCoord[0] = rd.randint(0, 99)  # location x
                randomCoord[1] = rd.randint(0, 99)  # location y

            infectionChance = rd.randint(1, 3)
            if (infectionChance == 3):
                infectedStatus = 2
                infectedCount += 1
            else:
                healthyCount += 1

            infectedStatus = 1
            new_cell = Cell(rd.randint(1, 80),  # age
                            infectedStatus,  # infection stat
                            randomCoord[0],  # location x
                            randomCoord[1],  # location y
                            rd.randint(0, 255),  # time virus
                            rd.randint(0, 255),  # time
                            self.grid)

            self.cell_dict[new_cell.Row, new_cell.Column] = new_cell
            self.grid[new_cell.Row, new_cell.Column] = new_cell.infectionStatus




    def show(self):
        for x in range(0, 100000):
            plt.imshow(self.grid)
            plt.title("Population: " + str(len(self.cell_dict)))
            #plt.xlabel("starting infection count = " + str(self.infectedCount))
            self.update_grid()
            plt.pause(0.000005)
            plt.clf()
        

