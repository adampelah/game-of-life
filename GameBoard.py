import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Slider, Button, RadioButtons
from matplotlib.text import Text
import random as rd
from Cell import Cell
import info


# from info import getTotalCases, getTotalDeaths, getDeathRate, getPopulation

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

    def relativePopulation(self, state):  # this function grabs population from census information
        return int(info.getPopulation(state) / self.size ** 2)

    def getPercentInfected(self, state):
        return float(info.getTotalCases(state) / info.getPopulation(state))

    def createPopulation(self, state):  # creates a population based on parameters and board

        self.population = self.relativePopulation(state)
        self.infectedCount = int(self.population * self.getPercentInfected(state))
        randomCoord = [0, 0]
        randomCoord[0] = (rd.randint(1, self.size - 1))  # location x
        randomCoord[1] = (rd.randint(1, self.size - 1))  # location y

        for x in range(0, self.population):

            infectionStatus = 1
            if x < self.infectedCount:  # this condition creates number of infected sells specified by parameters
                infectionStatus = 2

            # get random coordinates for cell
            while (self.grid[randomCoord[0], randomCoord[1]] != 0):
                randomCoord[0] = rd.randint(0, self.size - 1)  # location x
                randomCoord[1] = rd.randint(0, self.size - 1)  # location y

            # generate random cell
            new_cell = Cell(rd.randint(1, 80),  # age
                            infectionStatus,  # infection stat
                            randomCoord[0],  # location x
                            randomCoord[1],  # location y
                            rd.randint(0, 255),  # time
                            self)

            self.cell_list.append(new_cell)  # add cell to dictionary
            self.grid[new_cell.Row, new_cell.Column] = new_cell.infectionStatus  # add cell status to grid

    def update_grid(self):
        for index, cell in enumerate(self.cell_list):
            if (cell.time % 45 == 0):
                if (cell.deathRate()):
                    self.cell_list.pop(index)
            cell.move()

#-------------------------------Changes Below----------------------------------------------
    def setMilli(self, label):
        if label == 'Very Fast':
            millisec = 1
        if label == 'Fast':
            millisec = 2
        if label == 'Slow':
            millisec = 3

    def setFrames(self, val):
        frames = val

    def simulate(self, event):
        while len(self.cell_list) > self.population / 4:  # Visualize the grid
            plt.imshow(self.grid, 'cividis')
            plt.xticks([])
            plt.yticks([])
            plt.title("Population: " + str(len(self.cell_list)))
            #plt.xlabel("starting infection count = " + str(self.infectedCount))
            self.update_grid()
            plt.pause(0.0000005)
            plt.clf()

    def menu(self):
        plt.figtext(0.5, .85,'Germ Theory',color='#0e7a0d',fontsize='xx-large',
                    fontstyle='oblique',fontweight='heavy',horizontalalignment='center')

        state_ax = plt.axes([0.3, 0.6, 0.3, 0.1], fc='#ededed')
        state_box = TextBox(state_ax, 'Enter State: ', label_pad=0.05, hovercolor='#e3fbe3')
        state_box.on_submit(self.createPopulation)

        days_ax = plt.axes([0.3, 0.45, 0.5, 0.05], fc='#ededed')
        days_slider = Slider(days_ax, 'Number of days: ', 1, 90, valinit=45, valstep = 1)
        days_slider.on_changed(self.setFrames)

        speed_ax = plt.axes([0.3, 0.2, 0.15, 0.15], fc='#ededed')
        speed_buttons = RadioButtons(speed_ax,('Very Fast', 'Fast', 'Slow'))
        speed_buttons.on_clicked(self.setMilli)
        start_ax = plt.axes([0.67, 0.1, 0.2, 0.075], fc='#ededed')
        start_button = Button(start_ax, 'Start Simulation', hovercolor='#e3fbe3')
        start_button.on_clicked(self.simulate)
        plt.show()
