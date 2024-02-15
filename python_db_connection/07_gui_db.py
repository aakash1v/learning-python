from tkinter import *
import MySQLdb

def savedata(event):
    con = MySQLdb.Connect(host='localhost',user='root',password='root',database='dataflair')
    print('Connection success...')
    print('.....................')
    cur = con.cursor()
    sql = "insert into employee values (%d, '%s', '%s', %d)"
    values = (int(textid.get()),textname.get(),textdept.get(),int(textsal.get()))
    cur.execute(sql%values)
    print('Record inserted.. ',cur.rowcount)
    con.commit()
    con.close()
    print('Connection close')
    print('...................')

myroot = Tk()
myroot.geometry('600x600')
myroot.maxsize(600,600)
myroot.minsize(600,600)
myroot.title('Employee Registration Form....')



lb1= Label(text='Enter Employee Id : ',font=('Arial,10,bold'),fg='red')
lb1.grid(row=0,column=0)
empid=IntVar()
textid= Entry(textvariable=empid,font=('Arial,10,bold'),fg='blue')
textid.grid(row=0,column=1)

lb2= Label(text='Enter Name  : ',font=('Arial,10,bold'),fg='red')
lb2.grid(row=1,column=0)
empname=StringVar()
textname= Entry(textvariable=empname,font=('Arial,10,bold'),fg='blue')
textname.grid(row=1,column=1)

lb3= Label(text='Enter Department : ',font=('Arial,10,bold'),fg='red')
lb3.grid(row=2,column=0)
empdept=StringVar()
textdept= Entry(textvariable=empdept,font=('Arial,10,bold'),fg='blue')
textdept.grid(row=2,column=1)


lb4= Label(text='Enter Salary : ',font=('Arial,10,bold'),fg='red')
lb4.grid(row=3,column=0)
empsal=IntVar()
textsal= Entry(textvariable=empsal,font=('Arial,10,bold'),fg='blue')
textsal.grid(row=3,column=1)
textsal.bind('<Return>',lambda event: savedata(0))

btnsave = Button(text='save',font=('Arial,10,bold'),fg='blue',command=savedata)
btnsave.grid(row=4,column=1)


myroot.mainloop()



