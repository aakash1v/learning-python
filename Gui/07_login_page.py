from tkinter import *
myroot = Tk()
def checklogin():
    # print('This is check login method..')
    # print('Username : ',uname.get())
    # print('Password : ',upass.get())
    user = uname.get()
    pass1 = upass.get()
    if(user =='dataflair'and pass1 =='1234'):
        # print('login successfullly...')
        lb3['text']='login successfullly...'
        lb3['fg']='green'
    else:
        # print('invalid user or password...')
        lb3['text']='invalid user or password...'
        lb3['fg']='red'



myroot.title('Login Window')
myroot.geometry('400x200')

lb1 = Label(text='Username :',fg='blue',font=('Arial',10,'bold'))
lb2 = Label(text='Password :',fg='blue',font=('Arial',10,'bold'))
lb3 = Label(text='',font=('Arial',11,'bold'))
lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)
lb3.grid(row=3,column=0)


uname =StringVar()
upass =StringVar()
txtuser = Entry(textvariable=uname,font=('Arial',10,'bold'))
txtpass = Entry(textvariable=upass,font=('Arial',10,'bold'),show='*')
txtuser.grid(row=0,column=1)
txtpass.grid(row=1,column=1)
btn1 = Button(text='Login',font=('Arial',10,'bold'),fg='red',command=checklogin)
btn1.grid(row=2,column=0)


myroot.mainloop()