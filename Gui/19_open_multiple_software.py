from tkinter import *
import tkinter.filedialog as fd
import os

def opencalc():
    os.system('calc')

def openpaintb():
    os.system('mspaint')

def openword():
    os.system('start winword.exe')

def openexcel():
    os.system('start excel.exe')

def openpower():
    os.system('powerpnt')



myroot = Tk()
myroot.geometry('500x500')
myroot.title('Menu Demo')
# myroot.wm_iconbitmap(2.ico)
menubar = Menu(myroot)
myroot.config(menu=menubar)

filemenu=Menu(myroot,tearoff=0)
filemenu.add_command(label='Notepad',command=lambda: os.system('notepad'))
filemenu.add_command(label='Calculator',command=opencalc)
filemenu.add_command(label='Ms word',command=openword)
filemenu.add_command(label='Ms Excel',command=openexcel)
filemenu.add_command(label='Ms power point',command=openpower)
filemenu.add_command(label='Paint',command=openpaintb)
filemenu.add_command(label='Date',command=lambda: os.system('date'))
filemenu.add_separator()
filemenu.add_command(label='Exit',command=lambda: myroot.destroy())

menubar.add_cascade(label='File',menu=filemenu)



myroot.mainloop()