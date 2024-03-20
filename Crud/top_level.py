from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title("Master")

def func():
    top.destroy()

def func1():
    win.destroy()

top = Toplevel()
btn=Button(top,text='close window',command=func).pack()
btn1=Button(win,text='close window',command=func1).pack()


top.mainloop()