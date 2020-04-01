import sys
from GameBoard import Board

sys.path.append("..")

def main():
    b1 = Board()
    b1.fill_dict()
    b1.setUpGrid()
    b1.show()
       
main()
