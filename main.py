from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 800)

    maze1 = Maze(10, 10, 25, 25, 25, 25,win)
    win.wait_for_close()
    
main()

