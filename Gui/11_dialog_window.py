from tkinter import *
import tkinter.messagebox

def btnclick(n):
    if n==1:
        # choice = tkinter.messagebox.askyesno('Exit',"Are u sure want to exit ??")
        # 3 - TRue ,false, none
        choice = tkinter.messagebox.askokcancel('Exit',"Are u sure want to exit ??")
        if(choice==True):
            myroot.destroy()

    elif n==2:
        # tkinter.messagebox.showinfo("window",'REcord saved..succesfully!')
        # tkinter.messagebox.showerror("window",'REcord not saved.error!')
        tkinter.messagebox.showwarning("window",'REcord may loose..warning!')



myroot = Tk()
myroot.geometry('600x600')
myroot.maxsize(600,600)
myroot.minsize(600,600)
myroot.title('Message window..app')



fm = Frame(myroot,width=600,height=600,bg='Yellow')
fm.pack()
fm.propagate(0)

btnexit = Button(fm,text='Exit',command = lambda : btnclick(1))
btnexit.pack()
btnsave = Button(fm,text='Save',command = lambda : btnclick(2))
btnsave.pack()


myroot.mainloop()

