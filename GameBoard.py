import numpy as np
import matplotlib.pyplot as plt

class Board:
    sizeX = 2
    
    def __init__(self):
        self.board = np.matrix('0 0 0; 0 0 0; 0 0 0')
        self.store_y = 0
        self.store_x = 0
    
    def boardMove(self,x,y):
        self.board[self.store_x, self.store_y] = 0
        print ( x, y)
        self.board[x,y] = 1;
        self.store_x = x
        self.store_y = y

    def show(self):
        print(self.board.view(dtype=np.int16, type=np.matrix))
        

