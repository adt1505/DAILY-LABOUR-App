from tkinter import *
from PIL import ImageTk
import sqlite3
conn = sqlite3.connect('DL.db')

import tkinter  as tk 
from tkinter import * 
ws=Tk()

def confirm():
    ws.destroy()
    import confirm

img= PhotoImage(file='img12.png',master= ws)
img_label= Label(ws,image=img)
img_label.place(x=0, y=0)

ws.geometry("5000x5000") 
x=conn.execute('''SELECT * from delivery''');
i=0 # row value inside the loop 
for delivery in x: 
    for j in range(len(delivery)):
        e = tk.Label(ws,text=delivery[j],font=(50),width=25) 
        e.grid(row=i,column=j,padx=50,pady=50)
    
    for k in range(len(delivery)+1):
            b=Button(ws,text='SELECT',background='lightgreen',command=confirm,width=15,height=2)
            b.grid(row=i,column=j+1,padx=50)
    i=i+1

Label(ws,text="NAME",font=(10)).place(x=140,y=20)
Label(ws,text="ADDRESS",font=(10)).place(x=440,y=20)
Label(ws,text="DESCRIPTION",font=(10)).place(x=760,y=20)
Label(ws,text="AMOUNT",font=(10)).place(x=1120,y=20)

ws.mainloop()
