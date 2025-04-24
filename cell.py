from window import Window
from line import Line
from point import Point

class Cell():
    def __init__(self, x1, y1, x2, y2, window):
        self.win = window
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False

    def __eq__(self, other):
        if (self.x1 == other.x1 and self.x2 == other.x2 
            and self.y1 == other.y1 and self.y2 == other.y2
            and self.has_bottom_wall == other.has_bottom_wall
            and self.has_top_wall == other.has_top_wall 
            and self.has_left_wall == other.has_left_wall
            and self.has_right_wall == other.has_right_wall
            and self.visited == other.visited):
            return True
        return False

    def draw(self):
        if self.has_left_wall:
            fill_color = "red"
        else:
            fill_color = "white"
        point1 = Point(self.x1, self.y1)
        point2 = Point(self.x1, self.y2)
        line = Line(point1, point2)
        self.win.draw_line(line, fill_color)


        if self.has_right_wall:
            fill_color = "red"
        else:
            fill_color = "white"
        point1 = Point(self.x2, self.y1)
        point2 = Point(self.x2, self.y2)
        line = Line(point1, point2)
        self.win.draw_line(line, fill_color)

        if self.has_top_wall:
            fill_color = "red"
        else:
            fill_color = "white"
        point1 = Point(self.x1, self.y1)
        point2 = Point(self.x2, self.y1)
        line = Line(point1, point2)
        self.win.draw_line(line, fill_color)

        if self.has_bottom_wall == True:
            fill_color = "red"
        else:
            fill_color = "white"
        point1 = Point(self.x1, self.y2)
        point2 = Point(self.x2, self.y2)
        line = Line(point1, point2)
        self.win.draw_line(line, fill_color)
        
    def draw_move(self, to_cell, undo=False):
        center1X = (self.x1 + self.x2) / 2
        center1Y = (self.y1 + self.y2) / 2

        center2X = (to_cell.x1 + to_cell.x2) / 2
        center2Y = (to_cell.y1 + to_cell.y2) / 2

        center1 = Point(center1X, center1Y)
        center2 = Point(center2X, center2Y)

        line = Line(center1, center2)

        if undo == False:
            fill_color = "red"
        else:
            fill_color = "gray"
        


        
        

