import sys
sys.path.append("..")
from Cell import Cell
from GameBoard import Board

mainField = Board()
person = Cell ( 20, 0, 0, 0, 122, 0, mainField)
count = 0

while(count < 6):
    person.move()
    count+=1
