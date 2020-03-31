import sys
from Cell import Cell
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
sys.path.append("..")


def setUpGrid(grid, cell_dict):
    for x in range(0, 99):
        for y in range(0, 99):
            if (x, y) in cell_dict:
                grid[x][y] = cell_dict[x, y].infectionStatus  # Fill grid spot

def fill_grid(grid, cell_dict):
    

    for x in range(0, 99):
        for y in range(0, 99):
            if(x, y) in cell_dict:
                popped_cell = cell_dict.pop((x, y))
                grid[x][y] = 0
                popped_cell.move()  # call move on cell

                cell_dict[popped_cell.Row, popped_cell.Column] = popped_cell
                grid[popped_cell.Row][popped_cell.Column] = popped_cell.infectionStatus



def main():

    infectedCount = 0
    healthyCount = 0
    # CREATE GRID, POPULATE
    grid = np.zeros((100, 100))

    # CREATE dictionary of cells, accessed by row and col
    cell_dict = {}
    randomCoord = []
    randomCoord.append( rd.randint(0, 99)) # location x
    randomCoord.append( rd.randint(0, 99)) # location y
    
    for x in range(0, 200):

        while (grid[randomCoord[0], randomCoord[1]] != 0):
            randomCoord[0] = rd.randint(0, 99) # location x
            randomCoord[1] = rd.randint(0,99) # location y

        infectionChance = rd.randint(1,3)
        if(infectionChance == 3):
            infectedStatus = 2
            infectedCount += 1
        else:
            healthyCount += 1

        infectedStatus = 1
        new_cell = Cell(rd.randint(1, 80), # age
                        infectedStatus, # infection stat
                        randomCoord[0], # location x
                        randomCoord[1], # location y
                        rd.randint(0, 255), # time virus
                        rd.randint(0, 255), # time
                        grid) 

        cell_dict[new_cell.Row, new_cell.Column] = new_cell
        grid [new_cell.Row, new_cell.Column] = new_cell.infectionStatus


   
    setUpGrid(grid,cell_dict)
    for x in range(0, 100000):
        plt.imshow(grid)
        plt.title("Population: " + str(len(cell_dict)))
        plt.xlabel("starting infection count = " + str(infectedCount))
        fill_grid(grid, cell_dict)
        plt.pause(0.000005)
        plt.clf()
      
       
main()
