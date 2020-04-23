import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
    
    def __init__(self, inSize):  # creating parameter for user
        
        self.size = inSize
        self.grid = np.zeros((inSize, inSize))
        cell_list = []

    def relativePopulation(self, state): # this function grabs population from census information
        return int(info.getPopulation(state) / self.size **2)
    
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

            self.cell_list.append(new_cell)  # add cell to dictionary
            self.grid[new_cell.Row, new_cell.Column] = new_cell.infectionStatus  # add cell status to grid

    def update_grid(self, framenum, img,):
        for index, cell in enumerate(self.cell_list):
            if(cell.time % 45 == 0):
                if(cell.deathRate()):
                    self.cell_list.pop(index)
                    continue
            self.grid[self.size-1][self.size-1] = 2
            cell.move()
        img.set_data(self.grid)
        return img,




    def show(self):

        # Different version of plotting, use  def update_grid(self, framenum, img):
        frames = int(input("Enter amount of days to run simulation for: "))
        self.iterations = frames
        updateInterval = int(input("Enter amount of miliseconds per day: "))
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, interpolation='nearest')
        print("Running simulation...")
        ani = animation.FuncAnimation(fig, self.update_grid, fargs=(img, ),
                                      frames=frames,
                                      blit=True,
                                      interval=updateInterval)
        a = time.perf_counter()
        ani.save('lines.mp4', writer=writer)
        b = time.perf_counter()
        print("Runtime: ", b-a)
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
