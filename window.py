from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):                 
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("Maze")

        self.canvas = Canvas(self.root, height=self.height, width=self.width, bg="white")
        
        self.window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas.pack()



    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.window_running = True

        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)






