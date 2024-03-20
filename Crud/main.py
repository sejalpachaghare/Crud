import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk 

root = Tk() 
root.title("Student Registration System")
mt_tree = ttk.Treeview(root)

label=Label(root,text= "Student Registration System(CRUD MATRIX)",font=('Arial Bold',30))
label.grid(row=0,column=0,columnspan=3,rowspan=2,padx=50,pady=40)

root.mainloop()
