from tkinter import *

myroot = Tk()
myroot.title('My title...')
myroot.geometry('500x500')
mf = Frame(myroot,width=500,height=500,cursor='cross',bg='black')
# mf.propagate(0)
# mf.pack()

def reverse():
    n= mynum.get()
    s = 0
    while(n!=0):
        r = n%10
        s = s*10+r
        n = n//10
    lb2['text']= 'Reverse number is : {}'.format(s)

def factorial():
    n= mynum.get()
    f = 1
    while(n!=0):
        f = f*n 
        n= n-1

    lb2['text']= 'Factorial number is : {}'.format(f)



mynum = IntVar()
lb1 = Label(myroot,text='Enter a number :')
lb1.grid(row=0,column=0)
en1 = Entry(myroot,textvariable=mynum)
en1.grid(row=0,column=1)

btn1= Button(myroot,text='Factorial',command=factorial)
btn1.grid(row=1,column=0)
btn2= Button(myroot,text='Reverse',command=reverse)
btn2.grid(row=1,column=1)

lb2 = Label(myroot,text='',font=('Arial',15,'bold'))
lb2.grid(row=3,column=0)



myroot.mainloop()