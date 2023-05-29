from tkinter import *

THEME_COLOR = "#375362"

IMAGE_01 = "images/true.png"
IMAGE_02 = "images/false.png"


class Structure:

    def __init__(self):

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a label.
        self.label = Label()
        self.label.config(text="Score:", fg="white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.label.grid(row=0,column=1)

        # Create Canvas.
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="This is a simple text,just check what is happend.",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # Create True Button.
        self.true_button = Button()
        true_image = PhotoImage(file="images/true.png")
        self.true_button.config(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        # Create False Button.
        self.false_button = Button()
        false_image = PhotoImage(file="images/false.png")
        self.false_button.config(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
