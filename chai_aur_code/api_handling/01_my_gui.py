from tkinter import *
import test

myroot = Tk()

myroot.geometry('600x600')
myroot.title('Random books')

#main
title,author,desc,pagecount = test.random_book()
# print(f"Title : {title}\nAuthor : {author}\nDescription : {desc}\nPageCount : {pagecount}")
h1 = Label(myroot,text= "Book information...")
lb1 = Label(myroot,text=title,bg='yellow',fg='blue')
lb2 = Label(myroot,text=author,bg='yellow',fg='blue')
lb3 = Label(myroot,text=desc,bg='yellow',fg='blue')
lb4 = Label(myroot,text=pagecount,bg='yellow',fg='blue')

h1.pack()
lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()

myroot.mainloop()