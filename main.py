from window import Window
from point import Point
from line import Line


def main():
    win = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(300, 300)
    line1 = Line(point1, point2)
    win.draw_line(line1, "red")

    win.wait_for_close()
    
main()

