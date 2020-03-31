import sys
from Cell import Cell
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
sys.path.append("..")



def fill_grid(grid, cell_dict):
    for x in range(0, 100):
        for y in range(0, 100):
            if (x, y) in cell_dict:
                grid[x][y] = cell_dict[x, y].infectionStatus  # Fill grid spot

    for x in range(0, 100):
        for y in range(0, 100):
            if(x, y) in cell_dict:
                popped_cell = cell_dict.pop((x, y))
                grid[x][y] = 0
                popped_cell.move()  # call move on cell
                cell_dict[popped_cell.Row, popped_cell.Column] = popped_cell
                grid[popped_cell.Row%100][popped_cell.Column%100] = popped_cell.infectionStatus



def main():

    # CREATE dictionary of cells, accessed by row and col
    cell_dict = {}
    for x in range(0, 1000):
        new_cell = Cell(rd.randint(1, 80), rd.randint(0, 1), rd.randint(0, 100),
                    rd.randint(0, 100), rd.randint(0, 255), rd.randint(0, 255))
        cell_dict[new_cell.Row, new_cell.Column] = new_cell

    # CREATE GRID, POPULATE
    grid = np.zeros((100, 100))
    for x in range(0, 50):
        plt.imshow(grid)
        fill_grid(grid, cell_dict)
        plt.pause(0.05)
main()