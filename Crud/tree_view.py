# incomplete  error

from tkinter import *
from tkinter import ttk,messagebox,filedialog
import csv 
import os 
win = Tk()
win.title("Master")

def opencsv():
    global name 
    name = filedialog.askopenfilename(parent=win,initialdir=os.getcwd(),title='ab')
    filebtn.configure(text=name)
    with open (name) as f:
        reader = csv.DictReader(f,delimiter=',')
        for row in reader:
            mobile = row['Mobile Number']
            tree.insert('',0,values=(mobile))

scrollbarx = Scrollbar(win,orient=HORIZONTAL)
scrollbary = Scrollbar(win,orient=VERTICAL)

tree = ttk.Treeview(win,columns=('mobile number','status'),
                    height=25,selectmode='extended',
                    yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)

scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT,fill=Y)

scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM,fill=X)

tree.heading('Mobile Number',text='Mobile Number',anchor=W)
tree.heading('status',text='status',anchor=W)

tree.column('#0',stretch=NO,minwidth=0,width=0)
tree.column('#1',stretch=NO,minwidth=0,width=150)
tree.column('#2',stretch=NO,minwidth=0,width=150)

tree.pack()

filebtn = Button(win,text='Select CSV file',width=37,font='verdana 13 bold',command=opencsv)
filebtn.place(x=170,y=550)

win.mainloop() 