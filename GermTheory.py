import sys
from GameBoard import Board

sys.path.append("..")

def main():


    b1 = Board(100)  # Create board
    b1.createPopulation( 1000 , input("how many infected members: "))  # Create population
    b1.update_grid()  # Update grid
    b1.show()  # Show
       
main()
