from tkinter import *
win=Tk()
win.geometry('400x400')

ltitle=Label(win,text="LOGIN")
ltitle.grid(row=0,column=10,columnspan=4)

luname=Label(win,text="USERNAME")
luname.grid(row=1,column=9)

enuname=Entry(win,font=('arial',16))
enuname.grid(row=1,column=10)

lpasswd=Label(win,text="PASSWORD",font=('arial',16))
lpasswd.grid(row=3,column=9)

enpasswd=Entry(win,font=('arial',16))
enpasswd.grid(row=3,column=10)

btn=Button(win,text='submit',font=('arial',16))
btn.grid(row=5,column=10)

win.mainloop()
