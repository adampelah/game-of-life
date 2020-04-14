import sys
from GameBoard import Board

sys.path.append("..")

def main():


    b1 = Board(100)  # Create board
    b1.createPopulation( input("What state are you in? "))  # Create population
    b1.update_grid()  # Update gridFlo
    b1.show()  # Show
       
main()
