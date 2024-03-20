from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Master") 

scroll = Scrollbar(win) 
scroll.pack(side = RIGHT,fill=Y)

mylist = Listbox(win,yscrollcommand=Y)
for i in range(100):
    mylist.insert(END,i)
mylist.pack(side=LEFT,fill=Y)

scroll.config(command=mylist.yview)


win.mainloop()  
