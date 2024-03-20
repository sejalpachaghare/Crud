from tkinter import *

win = Tk()
win.title("Master")

# win.iconbitmap('icon2.png')
# win.maxsize(width=300,height=200)

#function
def func():
    x = var.get()
    # print(x)

    lbl.config(text="x",bg='red')


#label
lbl=Label(win,text="user name",bg="red",fg="white")
lbl.place(x=10,y=10)

lbl=Label(win,text="nothing",bg="red",fg="white")
lbl.place(x=40,y=120)

#pack
# lbl.pack() 
#grid
# lbl.grid(row=2,column=4)

#entry
var=StringVar()
ent=Entry(win,bg='red',fg='white',bd=5,textvariable=var)
ent.place(x=80,y=10)

#button
btn=Button(win,text="submit",bg="green",command=func)
btn.place(x=10,y=80)

win.mainloop() 