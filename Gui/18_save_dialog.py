from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as msg

def btnclick(choice):
    t=Text(myroot,width=100,height=100,fg='red')
    
    if(choice=='new'):
        t.pack()
    elif(choice=='save'):
        txtdata = str(t.get(1.0,END))
        filename = fd.asksaveasfile(parent=myroot,defaultextension='*.txt')
        with open(filename,'w') as f:
            f.write(txtdata)
    elif(choice=='exit'):
        ch = msg.askyesno('Exit','Are you sure want to exit ??')
        if ch==True:
            myroot.destroy()



myroot = Tk()
myroot.geometry('500x500')
myroot.title('Save window Demo')
# myroot.wm_iconbitmap(2.ico)
menubar = Menu(myroot)
myroot.config(menu=menubar)

filemenu=Menu(myroot,tearoff=0)
filemenu.add_command(label='New',command=lambda : btnclick('new'))
filemenu.add_command(label='Open',command=lambda : btnclick('open'))
filemenu.add_command(label='Save',command=lambda : btnclick('save'))
filemenu.add_separator()
filemenu.add_command(label='Exit',command=lambda : btnclick('exit'))

menubar.add_cascade(label='File',menu=filemenu)



myroot.mainloop()