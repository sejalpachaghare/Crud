# message box 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title("Master")


def func():
    if var.get()=='':
        messagebox.showwarning('Warning','Empty box')
    else:
        # messagebox.showinfo('Succeess',var.get()) 
        messagebox.askyesno('Title','do you want ot exit')

var = StringVar()
ent = Entry(win,textvariable=var)
ent.pack()

btn = Button(win,text='click me',command=func)
btn.pack()

win.mainloop()


