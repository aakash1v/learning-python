from tkinter import *

class MyEntry:
    def __init__(self,myroot):
        self.mf = Frame(myroot,width=500,height=500,cursor='cross',bg='yellow')
        self.mf.propagate(0)
        self.mf.pack()

        self.lb1 = Label(self.mf,text='Enter a string :')
        self.lb1.place(x=100,y=100)
        self.strv = StringVar()
        self.e1 = Entry(self.mf,textvariable=self.strv,show='*')
        self.e1.place(x=220,y=100)
        self.e1.bind('<Return>', self.display)

        #bottom
        self.lb2 = Label(self.mf,text='-',bg='Black',fg='white')
        self.lb2.place(x=200,y=200)

        self.btn1 = Button(self.mf,text='Click me',command= lambda : self.display(0))
        self.btn1.place(x=50,y=200)

    def display(self,event):
        s = self.strv.get()
        self.lb2['text'] = s.upper()

#calling place
myroot = Tk()
myroot.title('My entry...')
myroot.geometry('500x500')

m1 = MyEntry(myroot)


myroot.mainloop()