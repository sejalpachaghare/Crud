from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Master") 

def demo():
    pass 

my_menu = Menu(win)
win.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label='file',menu=file_menu) 
file_menu.add_cascade(label='New',command=demo)
file_menu.add_cascade(label='Open',command=demo)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='edit',menu=edit_menu)
edit_menu.add_cascade(label='undo',command=demo)
edit_menu.add_separator()
edit_menu.add_cascade(label='cut',command=demo)


win.mainloop()