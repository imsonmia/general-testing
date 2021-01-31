from tkinter import *
import sys


def exit_():
    cache_clear = open(file="usr_cache.txt", mode="w", buffering=1)
    cache_clear_2 = open(file="usr_cache.txt",mode="w", buffering=1)
    cache_clear.write('')
    cache_clear_2.write('')
    cache_clear.close()
    sys.exit()


class App:
    def __init__(self):
        shell = Tk()
        exit_btn = Button(shell, text="Exit", command=exit_)
        exit_btn.pack()
        shell.mainloop()
