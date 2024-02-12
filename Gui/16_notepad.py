# UNDER PROCESS...

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog as fd

def menuclick(choice):
    textbox=Text(myroot,width=800,height=500,font=('Arial,15,bold'),wrap=WORD)
    textbox.pack()
    if(choice=='new'):
        pass
    elif(choice=='new window'):
        filename = fd.askopenfilename(parent=myroot,title='Open file window',filetypes=(('Python file',"*.py"),('All files','*.*')))
        f = open(filename,'r')
        mytext = f.read()
        textbox.insert(1.0,mytext)
    elif(choice=='save'):
        filename = fd.asksaveasfile(parent=myroot,defaultextension='*.txt')
        content = str(textbox.get(1.0,END))
        f = open(filename,'w')
        f.write(content)
        f.close()


    elif(choice=='save as'):
        pass

myroot = Tk()
myroot.geometry('800x500')
myroot.title('Note_pad')
# myroot.wm_iconbitmap('img.ico')

menubar = Menu(myroot)
myroot.config(menu=menubar)
#filemenu
filemenu = Menu(myroot,tearoff=0)
filemenu.add_command(label='New',accelerator='Ctrl+N',command=lambda:menuclick('new'))
filemenu.add_command(label='New window',accelerator='Ctrl+Shift+N',command=lambda:menuclick('new window'))
filemenu.add_command(label='Save',accelerator='Ctrl+S',command=lambda:menuclick('save'))
filemenu.add_command(label='Save As',accelerator='Ctrl+Shift+S',command=lambda:menuclick('save as'))
filemenu.add_separator()
filemenu.add_command(label='Page Setup',accelerator='Ctrl+Shift+P')
filemenu.add_command(label='Print',accelerator='Ctrl+P')
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',command=lambda: myroot.destroy())
menubar.add_cascade(label='File',menu=filemenu)
#editmenu...
editmenu = Menu(myroot,tearoff=0)
editmenu.add_command(label='Cut',accelerator='Ctrl+X')
editmenu.add_command(label='Copy',accelerator='Ctrl+C')
editmenu.add_command(label='Paste',accelerator='Ctrl+V')
editmenu.add_command(label='Delete',accelerator='Ctrl+')
editmenu.add_separator()
editmenu.add_command(label='Find')
editmenu.add_command(label='Find Next')
editmenu.add_command(label='Find Previous')
editmenu.add_command(label='Replace')
editmenu.add_command(label='Goto')
menubar.add_cascade(label='Edit',menu=editmenu)



textbox =Text(myroot,width=800,height=500)
textbox.pack()


myroot.mainloop()