from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title("Master")

canvas = Canvas(win)

cord = 10,50,270,210 
canvas.create_arc(cord,start=0,extent=180,fill='red')
canvas.create_line(cord)
canvas.create_oval(cord) 

canvas.pack()

win.mainloop()