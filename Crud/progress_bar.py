from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Master") 

def bar():
    import time 
    progress['value'] = 100
    progress.update_idletasks()
    time.sleep(0.5) 


progress = ttk.Progressbar(win,orient=HORIZONTAL,length=100,mode='determinate')
progress.pack()

btn = Button(win,text='start',command=bar).pack()


win.mainloop()

