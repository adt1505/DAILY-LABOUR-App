from tkinter import *


ws = Tk()
img= PhotoImage(file='img12.png',master= ws)
img_label= Label(ws,image=img)
img_label.place(x=0, y=0)


ws.geometry('5000x5000')
ws.title('PROVIDER OR NEEDER')
ws['bg']='#5d8a82'

f = ("Times bold", 14)

def type():
    ws.destroy()
    import type

def type1():
    ws.destroy()
    import type1

def start():
    ws.destroy()
    import start


Button(ws,text="PROVIDER",background="AntiqueWhite2",command=type,width=30,height=2,font=(25)).place(x=550,y=300)
Button(ws,text="NEEDER",background="AntiqueWhite2",command=type1,width=30,height=2,font=(25)).place(x=550,y=400)
Button(ws,text="back",background="lightblue",command= start,width=9,height=1,font=(20)).place(x=630,y=650)


ws.mainloop()
