# Git VCS
# Last Edited 2021-01-26 07:48:35
from math import *
from tkinter import *
if __name__ == '__main__':
    sqrt_enable = False
    exp_enable = False
    add_enable = False
    calculations = [sqrt_enable, exp_enable, add_enable]


    def enable_sqrt():
        global sqrt_enable
        if sqrt_enable == False:
            sqrt_enable = True
            return sqrt_enable
        elif sqrt_enable == True:
            sqrt_enable = False
            return sqrt_enable

    def enable_exp():
        global exp_enable
        if exp_enable == False:
            exp_enable = True
            return exp_enable
        elif exp_enable == True:
            exp_enable = False
            return exp_enable

    def enable_add():
        global add_enable
        if add_enable == False:
            add_enable = True
            return add_enable
        elif add_enable == True:
            add_enable = False
            return add_enable

    def debug():
        print(sqrt_enable, exp_enable, add_enable)
        return

    def load_active_maths():
        for item in calculations:
            active_maths.insert(item)

    def calculate():
        return
    main = Tk()
    sqrt_btn = Button(main, text='SQRT', command=enable_sqrt)
    exp_btn = Button(main, text='EXPNT', command=enable_exp)
    add_btn = Button(main, text='ADD', command=enable_add)
    debug_btn = Button(main, text='DEBUG', command=debug)
    x_val = Entry(main)
    exp_val = Entry(main)
    add_val = Entry(main)
    x_val_note = Label(main, text='x:')
    exp_val_note = Label(main, text='Expnt:')
    add_val_note = Label(main, text='Add:')
    confirm_btn = Button(main, text='CONFIRM', command=load_active_maths)
    active_maths = Listbox(main)
    sqrt_btn.grid(row=3, column=2)
    exp_btn.grid(row=1, column=2)
    add_btn.grid(row=2, column=2)
    x_val.grid(row=0, column=1)
    exp_val.grid(row=1, column=1)
    add_val.grid(row=2, column=1)
    x_val_note.grid(row=0, column=0)
    exp_val_note.grid(row=1, column=0)
    add_val_note.grid(row=2, column=0)
    debug_btn.grid(row=4, column=2)
    confirm_btn.grid(row=5, column=2)
    active_maths.grid(row=6, column=0)
    main.mainloop()
