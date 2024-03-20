#radio button
from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Master")

def func():
    if var.get()==0:
        print('Male')
    else:
        print('Female')

var = IntVar()

radion=Radiobutton(win,text='Male',value=0,variable=var).pack()
radion=Radiobutton(win,text='Female',value=1,variable=var).pack()

btn = Button(win,text='Submit',command=func).pack()



win.mainloop()