from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import employeedao as empd



def clickbtn(value):
    if value =='save':
        ed = empd.MyDataBase()
        if (tkinter.messagebox.askyesno('save window','Are u sure want to save ??')):
            ed.insertData(int(textid.get()),textname.get(),textdept.get(),int(textsal.get()))
            tkinter.messagebox.showinfo('save','Record save successfully..')
            

    elif value =='search':
        eid= tkinter.simpledialog.askinteger('Search','Enter Employee id :')
        ed = empd.MyDataBase()
        E = ed.SearchData(eid)
        # tkinter.messagebox.showinfo('Result',"id = {}\nName = {}\nDepartment = {}\nSalary = {}".format(E.get_id(),E.get_name(),E.get_dept(),E.get_salary()))
        #setting searched value to textbox
        if (E!=None):
            empid.set(E.get_id())
            empname.set(E.get_name())
            empdept.set(E.get_dept())
            empsal.set(E.get_salary())
        else:
            tkinter.messagebox.showerror('No record','No record found..')

    elif value =='delete':
        eid= tkinter.simpledialog.askinteger('Search','Enter Employee id :')
        ed = empd.MyDataBase()
        E = ed.SearchData(eid)

        #setting searched value to textbox
        if (E!=None):
            empid.set(E.get_id())
            empname.set(E.get_name())
            empdept.set(E.get_dept())
            empsal.set(E.get_salary())
            choice = tkinter.messagebox.askokcancel('Delete window','Are u sure want to delete ??')
            if(choice):
                ed.deleteData(eid)
                tkinter.messagebox.showinfo('Delete','Record deleted...')
                #setting blank value
                empid.set("")
                empname.set("")
                empdept.set("")
                empsal.set("")

        else:
            tkinter.messagebox.showerror('No record','No record found..')

    elif value =='update':
        #underprocess..
        eid= tkinter.simpledialog.askinteger('Search','Enter Employee id :')
        ed = empd.MyDataBase()
        E = ed.SearchData(eid)

        if (E!=None):
            empid.set(E.get_id())
            empname.set(E.get_name())
            empdept.set(E.get_dept())
            empsal.set(E.get_salary())
        else:
            tkinter.messagebox.showerror('No record','No record found..')


    elif value=='exit':
        choice = tkinter.messagebox.askokcancel('exit','Are u sure want to exit ?? ')
        if (choice):
            myroot.destroy()
    


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

btnsave = Button(text='save',font=('Arial,10,bold'),fg='blue',command = lambda: clickbtn('save'))
btnsave.grid(row=4,column=0)

btnsearch = Button(text='search',font=('Arial,10,bold'),fg='blue',command = lambda: clickbtn('search'))
btnsearch.grid(row=4,column=1)

btnupdate = Button(text='update',font=('Arial,10,bold'),fg='blue',command = lambda: clickbtn('update'))
btnupdate.grid(row=4,column=2)

btndelete = Button(text='delete',font=('Arial,10,bold'),fg='blue',command = lambda: clickbtn('delete'))
btndelete.grid(row=4,column=3)

btnexit = Button(text='exit',font=('Arial,10,bold'),fg='blue',command = lambda: clickbtn('exit'))
btnexit.grid(row=4,column=4)

myroot.mainloop()



