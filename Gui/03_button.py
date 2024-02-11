from tkinter import *


def btnClick():
    print('Button is clicked...')
    if mf['bg']=='yellow':
        mf['bg']='red'
    else:
        mf['bg']='yellow'

myroot = Tk()
myroot.title('Buttons...')
myroot.geometry('500x500')
mf = Frame(myroot,width=500,height=500,cursor='cross',bg='yellow')
mf.propagate(0)
mf.pack()

btnblack = Button(mf,width = 5,height=2,text='REd',bg='red',fg='white',command=btnClick)
btnblack.pack()

myroot.mainloop()