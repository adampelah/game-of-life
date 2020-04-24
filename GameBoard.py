import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import TextBox, Slider, Button, RadioButtons
import random as rd
from Cell import Cell
import info
import cv2
import time
import timeit

matplotlib.use('TkAgg')


# from info import getTotalCases, getTotalDeaths, getDeathRate, getPopulation

class Board:
    # Core attributes
    size = 100
    grid = np.zeros((size, size))
    cell_list = []
    infectedCount = 0
    population = 0
    days = 45
    millisec = 100

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
        if (self.infectedCount < 50):
            self.infectedCount = 75

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

    def update_grid(self, framenum, img, ):
        for index, cell in enumerate(self.cell_list):
            if (cell.time % 45 == 0):
                if (cell.deathRate()):
                    self.cell_list.pop(index)
                    continue
            self.grid[self.size - 1][self.size - 1] = 2
            cell.move()
        img.set_data(self.grid)
        return img,

    def simulate(self, event):

        # Different version of plotting, use  def update_grid(self, framenum, img):
        self.iterations = self.days
        updateInterval = self.millisec
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, interpolation='nearest')
        plt.figtext(0.5, .1, 'Running simulation...', fontsize='large', horizontalalignment='center')
        ani = animation.FuncAnimation(fig, self.update_grid, fargs=(img,),
                                      frames=frames,
                                      blit=True,
                                      interval=updateInterval)
        a = time.perf_counter()
        ani.save('lines.mp4', writer=writer)
        b = time.perf_counter()
        runtime_ax = plt.axes([0.3, 0.87, 0.3, 0.1])
        runtime_box = TextBox(runtime_ax, 'Runetime: ', label_pab=0.05,)
        runtime_box.set_val(b - a)
        print("Runtime: ", b - a)
        cap = cv2.VideoCapture('lines.mp4')
        while True:

            ret, frame = cap.read()
            if ret == True:

                cv2.imshow('frame', frame)
                if cv2.waitKey(updateInterval) & 0xFF == ord('q'):
                    break

            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    def menu(self):
        plt.figtext(0.5, .85,'Germ Theory',color='#0e7a0d',fontsize='xx-large',
                    fontstyle='oblique',fontweight='heavy',horizontalalignment='center')

        state_ax = plt.axes([0.3, 0.6, 0.3, 0.1], fc='#ededed')
        state_box = TextBox(state_ax, 'Enter State: ', label_pad=0.05, hovercolor='#e3fbe3')
        state_box.on_submit(self.createPopulation)

        days_ax = plt.axes([0.3, 0.45, 0.5, 0.05], fc='#ededed')
        days_slider = Slider(days_ax, 'Number of days: ', 1, 90, valinit=45, valstep = 1)
        days_slider.on_changed(self.setDays)

        speed_ax = plt.axes([0.3, 0.2, 0.15, 0.15], fc='#ededed')
        speed_buttons = RadioButtons(speed_ax,('Very Fast', 'Fast', 'Slow'))
        speed_buttons.on_clicked(self.setMilli)
        start_ax = plt.axes([0.67, 0.1, 0.2, 0.075], fc='#ededed')

        start_button = Button(start_ax, 'Start Simulation', hovercolor='#e3fbe3')
        start_button.on_clicked(self.simulate)
        plt.show()

    def setMilli(self, label):
        if label == 'Very Fast':
            self.millisec=50
        if label == 'Fast':
            self.millisec=100
        if label == 'Slow':
            self.millisec=500

    def setDays(self, val):
            self.days = val
