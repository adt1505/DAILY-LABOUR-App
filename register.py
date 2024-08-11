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

ws.geometry('10000x10000')
ws.title('REGISTER')
ws['bg']='#ffbf00'

f = ("Times bold", 14)
def login():
    ws.destroy()
    import login

def start():
    ws.destroy()
    import start

def insertData():
    Username=e1.get()
    email=e2.get()
    phno=e3.get()
    gender=e4.get()
    password=e5.get()
    conpsd=e6.get()
    insert_query ="INSERT INTO `register`(`Username`,`email`,'phno','gender','password','conpsd')VALUES(?,?,?,?,?,?)"
    vals = (Username,email,phno,gender,password,conpsd)
    c.execute(insert_query,vals)
    conn.commit()
Button(ws,text="Save",background="lightgreen",command=insertData,width=15,height=1, font=(23)).place(x=550,y=450)

uname=Label(ws,text="Name",font=(50))
uname.place(x=400,y=50)
e1=Entry(width=30,font=(50))
e1.place(x=550,y=50)
email=Label(ws,text="Email",font=(50))
email.place(x=400,y=100)
e2=Entry(width=30,font=(50))
e2.place(x=550,y=100)
phno=Label(ws,text="Phone No.",font=(50))
phno.place(x=400,y=150)
e3=Entry(width=30,font=(50))
e3.place(x=550,y=150)
gender=Label(ws,text="Gender",font=(50))
gender.place(x=400,y=200)
e4=Entry(width=30,font=(50))
e4.place(x=550,y=200)
password=Label(ws,text="Password",font=(50))
password.place(x=400,y=250)
e5=Entry(show='*',width=30,font=(50))
e5.place(x=550,y=250)
conpsd=Label(ws,text="Confirm Password",font=(50))
conpsd.place(x=400,y=300)
e6=Entry(show='*',width=30,font=(50))
e6.place(x=550,y=300)

Button(ws,text="Submit",background="lightgreen",command=login,width=25,height=2,font=(23)).place(x=500,y=550)
Button(ws, text="back",command=start).place(x=600,y=650)

ws.mainloop()

