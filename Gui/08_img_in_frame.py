from tkinter import *
myroot = Tk()
myroot.title('My Image page...')
myroot.geometry('500x500')
myroot.maxsize(500,500)
myroot.minsize(500,500)

mf = Frame(myroot,width='500',height='500',bg='yellow',cursor='cross')
mf.propagate(0)
mf.pack()

# lb1 = Label(mf,width=40,height=2,text='Enter Student Id: ',bg='red')
# lb1.pack()
file1 =PhotoImage(file='/home/aakash/Desktop/python learning/Gui/lynx_landing.png')
#some time it not support jpg file..
lb2 = Label(mf,width=300,height=300,image=file1)
lb2.pack()



myroot.mainloop()

