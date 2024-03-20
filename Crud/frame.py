# frame  
from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Master")

topheader = Frame(win)
topheader.pack(side=TOP)

bottom = Frame(win)
bottom.pack(side=BOTTOM)

label = Label(topheader,text='This is header')
label.pack()

label = Label(bottom,text='This is bottom')
label.pack()

win.mainloop() 