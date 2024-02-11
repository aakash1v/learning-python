from tkinter import *


def btnClick(n):
    if n==1:
        mf['bg']='red'
    if n==2:
        mf['bg']='green'
    if n==3:
        mf['bg']='blue'
    if n==4:
        mf['bg']='black'

myroot = Tk()
myroot.title('Buttons...')
myroot.geometry('500x500')
mf = Frame(myroot,width=500,height=500,cursor='cross',bg='yellow')
mf.propagate(0)
mf.pack()

btnblack = Button(mf,width = 5,height=2,text='REd',bg='red',fg='white',command = lambda :  btnClick(1))
btnblack.pack()
btngreen= Button(mf,width = 5,height=2,text='REd',bg='green',command = lambda :  btnClick(2))
btngreen.pack()
btnblue = Button(mf,width = 5,height=2,text='REd',bg='blue',command = lambda :  btnClick(3))
btnblue.pack()
btnblack = Button(mf,width = 5,height=2,text='REd',bg='black',command = lambda :  btnClick(4))
btnblack.pack()

myroot.mainloop()