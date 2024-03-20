import tkinter as tk
from tkinter import ttk

#function coding 
exp = " " 
def press(num):
    global exp
    exp+=str(num)
    equation.set(exp)

def clear():
    global exp 
    exp = " "
    equation.set(exp)

def action():
    global exp 
    exp="Next Line :"
    equation.set(exp)

# end function coding 


key = tk.Tk()
# key.iconbitmap('87888.webp')
# key = tk.Tk()
key.title('Keyboard by Sejal')

#keyborad size 
key.geometry('1010x250')
key.maxsize(width=1330,height=350)
key.minsize(width=1330,height=350) 

#entry box 
equation = tk.StringVar()
Dis_entry = ttk.Entry(key,state='readonly',textvariable=equation)
Dis_entry.grid(rowspan=1,columnspan=100,ipadx=999,ipady=20) 

#background colour 
key.configure(bg='green')

# #button

# #first line 
q= ttk.Button(key,text='Q',command = lambda : press('Q'))
q.grid(row=1,column=0,ipadx=3,ipady=7) 

w= ttk.Button(key,text='W',command = lambda : press('W'))
w.grid(row=1,column=1,ipadx=3,ipady=7) 

e= ttk.Button(key,text='E',command = lambda : press('E'))
e.grid(row=1,column=2,ipadx=3,ipady=7) 

r= ttk.Button(key,text='R',command = lambda : press('R'))
r.grid(row=1,column=3,ipadx=3,ipady=7) 

t= ttk.Button(key,text='T',command = lambda : press('T'))
t.grid(row=1,column=4,ipadx=3,ipady=7) 

y= ttk.Button(key,text='Y',command = lambda : press('Y'))
y.grid(row=1,column=5,ipadx=3,ipady=7) 

u= ttk.Button(key,text='U',command = lambda : press('U'))
u.grid(row=1,column=6,ipadx=3,ipady=7) 

i= ttk.Button(key,text='I',command = lambda : press('I'))
i.grid(row=1,column=7,ipadx=3,ipady=7) 

o= ttk.Button(key,text='O',command = lambda : press('O'))
o.grid(row=1,column=8,ipadx=3,ipady=7) 

p= ttk.Button(key,text='P',command = lambda : press('P'))
p.grid(row=1,column=9,ipadx=3,ipady=7) 

cur= ttk.Button(key,text='[',command = lambda : press('['))
cur.grid(row=1,column=10,ipadx=3,ipady=7) 

cur_c= ttk.Button(key,text=']',command = lambda : press(']'))
cur_c.grid(row=1,column=11,ipadx=3,ipady=7) 

black_slach= ttk.Button(key,text='\\',command = lambda : press('\\'))
black_slach.grid(row=1,column=12,ipadx=3,ipady=7)


clear1 = ttk.Button(key,text='clear',width=6,command=clear)
clear1.grid(row=1,column=13,ipadx=3,ipady=7)


#second line 

a= ttk.Button(key,text='A',command = lambda : press('A'))
a.grid(row=2,column=0,ipadx=3,ipady=7) 

s= ttk.Button(key,text='S',command = lambda : press('S'))
s.grid(row=2,column=1,ipadx=3,ipady=7) 

d=ttk.Button(key,text='D',command = lambda : press('D'))
d.grid(row=2,column=2,ipadx=3,ipady=7) 

f=ttk.Button(key,text='F',command = lambda : press('F'))
f.grid(row=2,column=3,ipadx=3,ipady=7) 

g=ttk.Button(key,text='G',command = lambda : press('G'))
g.grid(row=2,column=4,ipadx=3,ipady=7) 

h=ttk.Button(key,text='H',command = lambda : press('H'))
h.grid(row=2,column=5,ipadx=3,ipady=7) 

j=ttk.Button(key,text='J',command = lambda : press('J'))
j.grid(row=2,column=6,ipadx=3,ipady=7) 

k=ttk.Button(key,text='K',command = lambda : press('K'))
k.grid(row=2,column=7,ipadx=3,ipady=7) 

l=ttk.Button(key,text='L',command = lambda : press('L'))
l.grid(row=2,column=8,ipadx=3,ipady=7) 

dout= ttk.Button(key,text=':',command = lambda : press(':'))
dout.grid(row=2,column=9,ipadx=3,ipady=7) 

string= ttk.Button(key,text='"',command = lambda : press('"'))
string.grid(row=2,column=10,ipadx=3,ipady=7) 


enter= ttk.Button(key,text='enter',width=6,command=action)
enter.grid(row=2,columnspan=165,ipadx=85,ipady=10) 


#third line 

key.mainloop()  
  
