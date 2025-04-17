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

    def draw(self):
        if self.has_left_wall:
            fill_color = "red"
            point1 = Point(self.x1, self.y1)
            point2 = Point(self.x1, self.y2)

            line = Line(point1, point2)

            self.win.draw_line(line, fill_color)
        if self.has_right_wall:
            fill_color = "red"
            point1 = Point(self.x2, self.y1)
            point2 = Point(self.x2, self.y2)

            line = Line(point1, point2)

            self.win.draw_line(line, fill_color)
        if self.has_top_wall:
            fill_color = "red"
            point1 = Point(self.x1, self.y1)
            point2 = Point(self.x2, self.y1)

            line = Line(point1, point2)

            self.win.draw_line(line, fill_color)
        if self.has_bottom_wall == True:
            fill_color = "red"
            point1 = Point(self.x1, self.y2)
            point2 = Point(self.x2, self.y2)

            line = Line(point1, point2)

            self.win.draw_line(line, fill_color)
