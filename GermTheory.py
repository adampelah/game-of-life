import sys
from Cell import Cell
from GameBoard import Board
import numpy as np
import random as rd
sys.path.append("..")
import matplotlib.pyplot as plt


def main():

    # mainField = Board()
    # person = Cell(20, 0, 0, 0, 122, 0, mainField)
    # count = 0
    #
    # while count < 6:
    #     person.move()
    #     count += 1

    # CREATE dictionary of cells, accessed by row and col
    cell_dict = {}
    for x in range(0, 1000):
        new_cell = Cell(rd.randint(1, 80), rd.randint(0, 1), rd.randint(0, 100),
             rd.randint(0, 100), rd.randint(0, 255), rd.randint(0, 255))
        cell_dict[new_cell.Row, new_cell.Column] = new_cell.infectionStatus

    # CREATE GRID, POPULATE
    grid = np.zeros((100, 100))
    for x in range(0, 100):
        for y in range(0, 100):
            if (x, y) in cell_dict:
                grid[x][y] = cell_dict[x, y]

    plt.imshow(grid)
    plt.show()
main()