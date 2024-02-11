from tkinter import *
class MyRadio:
    def __init__(self,myroot):
        self.mf = Frame(myroot,width=500,height=500,bg='yellow')
        self.mf.pack()
        self.mf.propagate(0)

        self.v= IntVar()
        self.rdm=Radiobutton(self.mf,text='Male',variable=self.v,value=1,font=("Arial",10,'bold'),command=self.rdclick)
        self.rdf=Radiobutton(self.mf,text='Female',variable=self.v,value=2,font=("Arial",10,'bold'),command=self.rdclick)

        self.lb1  =Label(self.mf,text='-',font=("Arial",10,'bold'))
        self.rdm.pack()
        self.rdf.pack()
        self.lb1.pack()


    def rdclick(self):
        if(self.v.get()==1):
            self.lb1['text']='Male'
            self.mf['bg']='red'
        else:
            self.lb1['text']='Female'
            self.mf['bg']='green'



myroot = Tk()
myroot.geometry('500x500')
myroot.maxsize(500,500)
myroot.minsize(500,500)
myroot.title('Radio button..demo')
# myroot.wm_iconbitmap('')

M1= MyRadio(myroot)

myroot.mainloop()