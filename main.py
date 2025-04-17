from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    win = Window(800, 600)

    cell1 = Cell(100,100, 200,200, win)
    cell1.draw()

    win.wait_for_close()
    
main()

