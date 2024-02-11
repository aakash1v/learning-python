from tkinter import *

class MyTable:
    def __init__(self,myroot):
        for i in range(5):
            for j in range(4):
                self.e = Entry(myroot,width=10,fg='blue',font=('Arial,12,blue'))
                self.e.grid(row=i,column=j)
                self.e.insert(END,mylist[i][j])


mylist= [('Emp No','Emp Name','Salary','Depart.'),(101,'Aakash',10000,'It'),(102,'Manohar',2000000,'Sales'),(103,'Ankush',450990,'Analytics'),(104,'Ankush',450990,'Analytics')]


myroot = Tk()
myroot.geometry('500x500')
myroot.title('Table....')

M1= MyTable(myroot)
myroot.mainloop()