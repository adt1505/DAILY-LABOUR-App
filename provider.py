from tkinter import *
import sqlite3
conn=sqlite3.connect('DL.db')
print("Opened database successfully");
c = conn.cursor()

ws = Tk()
ws.geometry('500x5000')
ws.title('PROVIDER')
ws['bg']='#ffbf00'

f = ("Times bold", 14)
c = conn.cursor()

def insertData():
    name =e1.get()
    address=e2.get()
    job_discription=e3.get()
    amount=e4.get()
    insert_query ="INSERT INTO `daycare`(`name`, `address`, `job_discription`, `amount`)VALUES (?,?,?,?)"
    vals = (name,address,job_discription,amount)
    c.execute(insert_query,vals)
    conn.commit()

Button(ws,text="Save",background="lightgreen",command=insertData,width=15,height=2, font=(23)).pack( expand=TRUE, side=LEFT)

def provider_needer():
    ws.destroy()
    import provider_needer

uname=Label(ws,text="Name",font=(23))
uname.place(x=100,y=150)
e1=Entry(width=20,font=(20))
e1.place(x=220,y=150)
add=Label(ws,text="Address",font=(23))
add.place(x=100,y=200)
e2=Entry(width=20,font=(20))
e2.place(x=220,y=200)
jobdesc=Label(ws,text="Job discription",font=(23))
jobdesc.place(x=100,y=250)
e3=Entry(width=20,font=(20))
e3.place(x=220,y=250)
amt=Label(ws,text="Pay Amount",font=(23))
amt.place(x=100,y=300)
e4=Entry(width=20,font=(20))
e4.place(x=220,y=300)

Button(ws,text="back",background="lightblue",command=provider_needer,width=9,height=3,font=(20)).place( x=215,y=680)

ws.mainloop()
