import time
from cell import Cell
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        self.win = win
        self.create_cells()
        if seed != None:
            self.seed = random.seed(seed)

        self.break_entance_exit()
        self.break_walls_f(0,0)
        self.reset_visited()
        
   
    def reset_visited(self):
        for i in range(len(self.cells)):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False
    

    def create_cells(self):
        self.cells = [[] for i in range(self.num_cols)]

        for i in range(len(self.cells)):
            for j in range(self.num_rows):
                self.draw_cell(i,j)

    def draw_cell(self, i,j):
        maze_start_x = self.x1
        maze_start_y = self.y1

        x1 = maze_start_x + (self.cell_size_x*(i+1))
        y1 = maze_start_y + (self.cell_size_y*(j+1))

        x2 = maze_start_x + (self.cell_size_x*(i+1)) + self.cell_size_x
        y2 = maze_start_y + (self.cell_size_y*(j+1)) + self.cell_size_y

        self.cells[i].append(Cell(x1,y1,x2,y2,self.win))
        self.cells[i][j].visited = False
        self.cells[i][j].draw()
        self.animate()


    def animate(self):
        self.win.redraw()
        time.sleep(0.005)

        

    def break_entance_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[0][0].has_left_wall = False
        self.cells[0][0].draw()
    
        self.cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self.cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.cells[self.num_cols-1][self.num_rows-1].draw()

    def break_walls_f(self, i, j):
        self.cells[i][j].visited = True
        while True:
            to_visit = []

            if i < self.num_cols-1 and self.cells[i+1][j].visited == False:
                to_visit.append((i+1, j))
            if i > 0 and self.cells[i-1][j].visited == False:
                to_visit.append((i-1, j))
            if j < self.num_rows-1 and self.cells[i][j+1].visited == False:
                to_visit.append((i, j+1))
            if j > 0 and self.cells[i][j-1].visited == False:
                to_visit.append((i, j-1))
            if len(to_visit) == 0:
                self.cells[i][j].draw()
                self.animate()
                return
            
            
            rand = random.randrange(len(to_visit))
            choice = to_visit[rand]
            

            if choice[0] == i+1:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
                self.cells[i][j].draw()
                self.animate()

            if choice[1] == j+1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
                self.cells[i][j].draw()
                self.animate()

            if choice[0] == i-1:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
                self.cells[i][j].draw()
                self.animate()

            if choice[1] == j-1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
                self.cells[i][j].draw()
                self.animate()

            
            self.break_walls_f(choice[0], choice[1])


            



            

            
            
        


        
        
        


            
            





           
        

    
            





