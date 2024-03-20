# list box 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title("Master")

def funct():
    lst.delate(ANCHOR)

lst = Listbox(win,width=27) 

items=['Apple','Banana','Orange']

for i in items:
    lst.insert(END,i)
btn = Button(win,text='Delate',command=funct).pack()

lst.pack()


win.mainloop()
