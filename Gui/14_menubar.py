from tkinter import *
myroot = Tk()
myroot.geometry('600x600')
myroot.title('Menu Demo Application...')

menubar = Menu(myroot)
myroot.config(menu = menubar)

filemenu = Menu(myroot,tearoff=0)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=myroot.destroy)
menubar.add_cascade(label='File Menu',menu=filemenu)

editmenu = Menu(myroot,tearoff=0)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Delete')
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_separator()





myroot.mainloop()