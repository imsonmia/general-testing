from tkinter import *
import sys


def exit_():
    sys.exit()


class App:
    def __init__(self):
        shell = Tk()
        exit_btn = Button(shell, text="Exit", command=exit_)
        exit_btn.pack()
        shell.mainloop()
