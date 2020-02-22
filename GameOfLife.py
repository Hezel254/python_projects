#this game enables the random existance of cells and their life is majorly detemined 
#by the neighbouring cells. An initial state of the cell is chosen to be dead

#here we should have a class for the cell and various methods representing the state.

#setting the initial state of the cell to be dead
#PART 1, defining the cells

class Cell:
    def __init__(self):
        ''' setting the initial state of the cell to be dead'''
        self.status = 'Dead'
        
    def set_dead(self):
        #checking if the cells satutus is dead
        self.status = 'Dead'
    def set_alive(self):
      self.status = 'Alive'
    def is_alive (self):
        if self.status == 'Alive':
            return True
        return False
    def get_print_character(self):
        if self.is_alive():
            return 'O'
        return '*'
    
    #part 2, we now write the board
from cell import Cell
from random import randint

class Board:
    def __init__(self, rows,columns):
        self.rows = rows
        self.columns = columns
        self.grid[X][Y] = [[cell()for column_cells in range (self.columns)] for row in row_cells in range (self.rows)]
        self.generate_board()
    def draw_board(self):
        print('\n'*10)
        print('printing board')
        for row in self.grid:
            for column in row:
                #there's a 33%chance that the cell will spawn alive
                chance_number == 1
                column.set_alive()
