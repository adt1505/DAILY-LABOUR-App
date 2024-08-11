from tkinter import *
from PIL import ImageTk
import sqlite3
conn=sqlite3.connect('DL.db')
print("Opened database successfully");
c = conn.cursor()


ws = Tk()
img= PhotoImage(file='img12.png',master= ws)
img_label= Label(ws,image=img)
img_label.place(x=0, y=0)

ws.geometry('5000x5000')
ws.title('LOGIN')
ws['bg']='#5d8a82'

def provider_needer():
    ws.destroy()
    import provider_needer

def start():
    ws.destroy()
    import start

def insertData():
    Username=e1.get()
    Password=e2.get()
    insert_query ="INSERT INTO `login`(`Username`,`Password`)VALUES(?,?)"
    vals = (Username,Password)
    c.execute(insert_query,vals)
    conn.commit()

Button(ws,text="Save",background="lightgreen",command=insertData,width=15,height=2, font=(23)).place(x=590,y=300)
    
uname=Label(ws,text="Username",font=(23))
uname.place(x=500, y=150)
e1=Entry(width=25,font=(20))
e1.place(x=600,y=150)

password=Label(ws,text="Password",font=(23))
password.place(x=500, y=200)
e2=Entry(show='*',width=25,font=(20))
e2.place(x=600,y=200)


Button(ws,text="LOGIN",background="lightgreen",command=provider_needer,width=25,height=2,font=(20)).place(x=550,y=400)
Button(ws,text="back",background="lightblue",command= start,width=9,height=1,font=(20)).place(x=620,y=650)


ws.mainloop()

