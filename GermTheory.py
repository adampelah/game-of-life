import sys
from GameBoard import Board

sys.path.append("..")

def main():
    b1 = Board(100)
    b1.createPopulation(1000, 25)
    b1.update_grid()
    b1.show()
       
main()
