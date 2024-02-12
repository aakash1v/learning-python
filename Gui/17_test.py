from tkinter import *

def btnclick():
    subwindow=Toplevel(window)
    subwindow.title('this is sub window..')
    subwindow.geometry('200x100')
    Label(subwindow,text='This is sub winow page').pack()
 
    subwindow.mainloop()
    

window = Tk()
window.geometry('300x300')
window.title('Open window from anoter..')
lb1= Label(window,text='This is main window page..',fg='red')
btn1 = Button(window,text='Click here for sub window',command=btnclick)

lb1.pack()
btn1.pack()




window.mainloop()