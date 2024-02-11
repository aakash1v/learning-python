from tkinter import *

class MyClass:
    def __init__(self,myroot):
        self.mf = Frame(myroot,width=500,height=500)
        self.mf.pack()
        self.mf.propagate(0)
        self.btn1= Button(self.mf,text='Red',bg='red',command= lambda :self.myclick(0))
        self.btn2= Button(self.mf,text='Green',bg='green',command= lambda :self.myclick(1))
        self.btn3= Button(self.mf,text='Blue',bg='blue',command= lambda :self.myclick(2))
        self.btn4= Button(self.mf,text='Black',bg='Black',fg='white',command= lambda :self.myclick(3))

        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()
    
    def myclick(self,n):
        if(n==0):
            self.mf['bg']='red'
        elif n==1:
            self.mf['bg']='green'
        elif n==2:
            self.mf['bg']='blue'
        elif n==3:
            self.mf['bg']='black'
        else:
            self.mf['bg']='yellow'

myroot = Tk()
myroot.title('Button Gui app..')
myroot.geometry('500x500')
M1 = MyClass(myroot)
myroot.mainloop()

