from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as msg

def clickmenu(choice):
    if(choice=='open'):
        filename = fd.askopenfilename(parent=myroot,title='Open file window',filetypes=(('Python file',"*.py"),('All files','*.*')))
        f = open(filename,'r')
        mytext = f.read()
        t= Text(myroot,width=100,height=50,fg='red',wrap=WORD)
        t.pack()
        t.insert(1.0,mytext)
        f.close()


    elif(choice=='exit'):
        ch = msg.askyesno('Exit','Are you sure want to exit??')
        if ch==True:
            myroot.destroy()


myroot = Tk()
myroot.geometry('600x600')
myroot.title('My notepad application...')

menubar = Menu(myroot)
myroot.config(menu= menubar)

myfilemenu= Menu(myroot,tearoff=0)
myfilemenu.add_command(label='Open',command=lambda : clickmenu('open'))
myfilemenu.add_command(label='Exit',command=lambda : clickmenu('exit'))
myfilemenu.add_separator()
myfilemenu.add_checkbutton(label='Bold')

menubar.add_cascade(label="File",menu=myfilemenu)







myroot.mainloop()