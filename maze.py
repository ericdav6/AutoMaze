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
        self.solve()
        
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
        self.animate_maze_creation()

    def animate_maze_creation(self):
        self.win.redraw()
        time.sleep(0.001)
    
    def animate_solve(self):
        self.win.redraw()
        time.sleep(0.02)

    def break_entance_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[0][0].has_left_wall = False
        self.cells[0][0].draw()
    
        self.cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self.cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.cells[self.num_cols-1][self.num_rows-1].draw()

    def solve(self):
        return(self.solve_r(0,0))
    
    def solve_r(self, i, j):
        self.animate_solve()
        self.cells[i][j].visited = True

        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        else:
            if i > 0 and self.cells[i-1][j].visited == False and self.cells[i][j].has_left_wall == False:
                self.cells[i][j].draw_move(self.cells[i-1][j])
                if self.solve_r(i-1, j):
                    return True
                self.cells[i][j].draw_move(self.cells[i-1][j], True)

            if i < self.num_cols-1 and self.cells[i+1][j].visited == False and self.cells[i][j].has_right_wall == False:
                self.cells[i][j].draw_move(self.cells[i+1][j])
                if self.solve_r(i+1, j):
                    return True
                self.cells[i][j].draw_move(self.cells[i+1][j], True)

            if j > 0 and self.cells[i][j-1].visited == False and self.cells[i][j].has_top_wall == False:
                self.cells[i][j].draw_move(self.cells[i][j-1])
                if self.solve_r(i, j-1):
                    return True
                self.cells[i][j].draw_move(self.cells[i][j-1], True)

            if j < self.num_rows-1 and self.cells[i][j+1].visited == False and self.cells[i][j].has_bottom_wall == False:
                self.cells[i][j].draw_move(self.cells[i][j+1])
                if self.solve_r(i, j+1):
                    return True
                self.cells[i][j].draw_move(self.cells[i][j+1], True)
                
            return False
        
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
                self.animate_maze_creation()
                return
            
            
            rand = random.randrange(len(to_visit))
            choice = to_visit[rand]
            

            if choice[0] == i+1:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
                self.cells[i][j].draw()
                self.animate_maze_creation()

            if choice[1] == j+1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
                self.cells[i][j].draw()
                self.animate_maze_creation()

            if choice[0] == i-1:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
                self.cells[i][j].draw()
                self.animate_maze_creation()

            if choice[1] == j-1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
                self.cells[i][j].draw()
                self.animate_maze_creation()

            
            self.break_walls_f(choice[0], choice[1])


            



            

            
            
        


        
        
        


            
            





           
        

    
            





