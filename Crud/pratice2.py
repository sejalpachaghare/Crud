# combobox
from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Master")

var =StringVar()

com =ttk.Combobox(win,width=27)
com.place(x=10,y=10)
com['state']='readonly'
com['values'] =('Jan',
                'Feb',
                'March')
com.current(0)
win.mainloop() 