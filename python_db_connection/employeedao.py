import MySQLdb
import model


class MyDataBase:
    def __init__(self):
        self.con = MySQLdb.Connect(host= 'localhost',user = 'root',password='root',database='dataflair')
        print('Connection success....')
        self.cur = self.con.cursor()

    def insertData(self,eid,ename,edept,esalary):
        sql = "insert into employee values(%d,'%s' ,'%s',%d)"
        self.value= (eid,ename,edept,esalary)
        self.cur.execute(sql%self.value)
        print('Record inserted ',self.cur.rowcount)
        self.con.commit()
        print('Inserted successfully')

    def SearchData(self,eid):
        sql = "select * from employee where eid=%d"
        self.cur.execute(sql%eid)
        if (self.cur.rowcount>0):
            result = self.cur.fetchone()
            E1 = model.Employee()
            E1.insert(result[0],result[1],result[2],result[3])
            return E1
        
    def updateData(self,E):
        sql = "update employee set name='%s', dept= '%s',salary = %d where eid= %d "
        value = (E.get_getname,E.get_dept,E.get_salary)
        self.cur.execute(sql%value)
        self.con.commit()
        
    def deleteData(self,eid):
        sql = "delete from employee where eid=%d"
        self.cur.execute(sql%eid)
        self.con.commit()
        


    def conClose(self):
        self.con.close()

#Calling place
# eid = int(input('Enter employeee id :'))
# ename = input('Enter Emplyee Name :')
# edept= input('Enter department Name :')
# esal = int(input('Enter salary'))

# M1 = MyDataBase()
# M1.insertData(eid,ename,edept,esal)
# M1.conClose()