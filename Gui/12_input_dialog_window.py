from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

def btnclick():
    name =tkinter.simpledialog.askstring('Name box ','Enter your name :')
    age =tkinter.simpledialog.askinteger('Age box','Enter your age :')
    per = tkinter.simpledialog.askfloat('Per box','Enter your percentage :')
    tkinter.messagebox.showinfo('display','Name is = {}\nAge is = {} \nper is = {}'.format(name,age,per))


myroot= Tk()
myroot.geometry('600x600')
myroot.title('Input Dialog box..')
myroot.maxsize(600,600)
myroot.minsize(600,600)

mf = Frame(myroot,width=600,height=600,bg='yellow')
mf.pack()
mf.propagate(0)

btninput = Button(mf,text = 'Click',font=('Arial,10,bold'),fg='red',command=btnclick)
btninput.pack()




myroot.mainloop()