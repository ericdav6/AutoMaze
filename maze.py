import time
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        self.win = win

        self.create_cells()

    def create_cells(self):
        self.cells = [[[] for i in range(self.num_rows)] for j in range(self.num_cols)]

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.draw_cell(i,j)

    def draw_cell(self, i,j):
        maze_start_x = self.x1
        maze_start_y = self.y1

        x1 = maze_start_x + (self.cell_size_x*(i+1))
        y1 = maze_start_y + (self.cell_size_y*(j+1))

        x2 = maze_start_x + (self.cell_size_x*(i+1)) + self.cell_size_x
        y2 = maze_start_y + (self.cell_size_y*(j+1)) + self.cell_size_y

        self.cells[i][j].append(Cell(x1,y1,x2,y2,self.win))
        self.cells[i][j][0].draw()
        self.animate()


    def animate(self):
        self.win.redraw()
        time.sleep(0.05)


