import MySQLdb

class MyDataBase:
    def __init__(self):
        self.con = MySQLdb.Connect(host= 'localhost',user = 'root',password='root',database='dataflair')
        print('Connection success....')

    def insertData(self,eid,ename,edept,esalary):
        sql = "insert into employee values(%d,'%s' ,'%s',%d)"
        self.value= (eid,ename,edept,esalary)
        self.cur = self.con.cursor()
        self.cur.execute(sql%self.value)
        print('Record inserted ',self.cur.rowcount)
        self.con.commit()
        print('Inserted successfully')

    def conClose(self):
        self.con.close()

#Calling place
eid = int(input('Enter employeee id :'))
ename = input('Enter Emplyee Name :')
edept= input('Enter department Name :')
esal = int(input('Enter salary'))

M1 = MyDataBase()
M1.insertData(eid,ename,edept,esal)
M1.conClose()