from tkinter import *
from tkinter import font

myroot = Tk()
myroot.title('Student Login SEction')
# myroot.wm_iconbitmap("p1.ico")
myroot.geometry('500x500')
fm = Frame(myroot,width=700,height=700,bg='yellow',cursor='cross')
# fm.propagate(0)
# fm.pack()

# mylist = list(font.families())
# for s in mylist:
#     print(s)
'''font changing...'''
lb1 = Label(text = 'Thi is a test Font',fg="red",font=('Script MT Bold',10,'bold'))
lb1.pack()

myroot.mainloop()

