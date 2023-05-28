from tkinter import *

THEME_COLOR = "#375362"


class Structure:

    def __int__(self):

        self.window = Tk()
        self.window.title(string="Quizzer")
        self.window.config(padx=20, pady=20,)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        # self.canvas.canvas.create_text(250, 10, text="Score: ", width=250, font=("Arial", 15, "bold"))
        self.canvas.create_text(150,125,text="This is a simple text", font=("Arial", 20, "italic"))
        self.canvas.grid(row=0, column=0)


        self.window.mainloop()

