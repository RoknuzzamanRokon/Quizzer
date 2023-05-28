from tkinter import *

THEME_COLOR = "#375362"


class Structure:
    def __int__(self):

        self.window = Tk()
        self.window.title(string="Quizzer")
        self.window.config(padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config()
        self.canvas.grid(row=0, column=0)


        self.window.mainloop()

