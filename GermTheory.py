import sys
from Cell import Cell
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
sys.path.append("..")



def fill_grid(grid, cell_dict):
    for x in range(0, 99):
        for y in range(0, 99):
            if (x, y) in cell_dict:
                grid[x][y] = cell_dict[x, y].infectionStatus  # Fill grid spot

    for x in range(0, 99):
        for y in range(0, 99):
            if(x, y) in cell_dict:
                popped_cell = cell_dict.pop((x, y))
                grid[x][y] = 0
                popped_cell.move()  # call move on cell
                cell_dict[popped_cell.Row, popped_cell.Column] = popped_cell
                grid[popped_cell.Row][popped_cell.Column] = popped_cell.infectionStatus



def main():

    # CREATE GRID, POPULATE
    grid = np.zeros((100, 100))

    # CREATE dictionary of cells, accessed by row and col
    cell_dict = {}
    randomCoord = []
    randomCoord.append( rd.randint(0, 99)) # location x
    randomCoord.append( rd.randint(0, 99)) # location y
    
    for x in range(0, 1000):

        while (grid[randomCoord[0], randomCoord[1]] != 0):
            randomCoord[0] = rd.randint(0, 99) # location x
            randomCoord[1] = rd.randint(0,99) # location y

        new_cell = Cell(rd.randint(1, 80), # age
                        rd.randint(1, 2), # infection stat
                        randomCoord[0], # location x
                        randomCoord[1], # location y
                        rd.randint(0, 255), # time virus
                        rd.randint(0, 255), # time
                        grid) 

        cell_dict[new_cell.Row, new_cell.Column] = new_cell
        grid [new_cell.Row, new_cell.Column] = new_cell.infectionStatus


   
    for x in range(0, 100000):
        plt.imshow(grid)
        fill_grid(grid, cell_dict)
        plt.pause(0.000005)
        plt.clf()
        print("number of cells on the board: " + str(len(cell_dict)))
main()
