from tkinter import *

win = Tk()
win.title("Master")

file= PhotoImage(file='icon2.png')

label =Label(win,image=file)
label.pack()

win.mainloop()