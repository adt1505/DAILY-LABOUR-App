from tkinter import *
from PIL import ImageTk

ws = Tk()
img= PhotoImage(file='img12.png',master= ws)
img_label= Label(ws,image=img)
img_label.place(x=0, y=0)

ws.geometry('10000x10000')
ws.title('thankyou')
ws['bg']='Cadetblue4'

Label(ws,text="THANK YOU!!",font=("Comic Sans MS",20,"bold")).place(x=620,y=500)
Label(ws,text="FOR CHOOSING US",font=("Comic Sans MS",18,"bold")).place(x=590,y=580)
Label(ws,text="DAILY LABOUR",font=("Comic Sans MS",20,"bold")).place(x=620,y=50)

ws.mainloop()
