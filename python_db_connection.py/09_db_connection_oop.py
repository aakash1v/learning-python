import MySQLdb
import model


class MyDataBase:
    def __init__(self):
        self.con = MySQLdb.Connect(host= 'localhost',user = 'root',password='root',database='dataflair')
        print('Connection success....')
        self.cur = self.con.cursor()

    def autoId(self):
        maxid = 100
        sql = "Select max(eid) from  employee " 
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.maxid = result[0]
        self.maxid +=1
        return self.maxid

    def insertData(self,ename,edept,esalary):
        self.autoId()
        sql = "insert into employee values(%d,'%s' ,'%s',%d)"
        self.value= (self.maxid,ename,edept,esalary)
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
        print('Record deleted....')

    def deleteId(self,eid):
        sql = "Select * from employee where eid = %d"
        self.cur.execute(sql%eid)
        row = self.cur.fetchone()
        if (self.cur.rowcount !=0 ):
            print('.......................')
            print('id       Name        Department      Salary')
            print("%d   %s  %s      %d"%(row[0],row[1],row[2],row[3]))
            if input('Are u sure want to delete ?? ').lower().startswith('y'):
                self.deleteData(eid)


        else:
            print('No recod found...')
        
    # def __del__(self):
    #     self.con.close() 
    #     print('Connection closed...')

    def searchAll(self):
        sql = "Select * from employee"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print('.......................')
        print('id       Name        Department      Salary')
        for row in result:
            print("%d   %s  %s      %d"%(row[0],row[1],row[2],row[3]))
            print('...................................')

    # def conClose(self):
    #     self.con.close()

#Calling place

# eid = int(input('Enter employeee id :'))


'''M1 = MyDataBase()
m = M1.autoId()
print(m)
ename = input('Enter Emplyee Name :')
edept= input('Enter department Name :')
esal = int(input('Enter salary'))
M1.insertData(ename,edept,esal)'''
# M1.con.Close()
'''
M1 = MyDataBase()
# M1.searchAll()
eid = int(input('Enter id to delete :'))
M1.deleteId(eid)'''



while(True):
    m1 = MyDataBase()
    print(".................Database Menu...................")
    print("1. Insert DAta\n2. Search REcord by Id\n3. SEarch record \n4. Delete by Id\n 5. Exit")
    print('..................')
    ch = int(input('Enter your choice ..'))
    if ch ==1:
        ename = input('Enter Emplyee Name :')
        edept= input('Enter department Name :')
        esal = int(input('Enter salary'))
        m1.insertData(ename,edept,esal)

    elif ch ==2:
        eid =int(input("Enter Employee id  for search"))
        result = m1.SearchData(eid)
        print("{} , {} , {}, {} ".format(result.get_id(),result.get_name(),result.get_dept(),result.get_salary()))


    elif ch ==3:
        m1.searchAll()

    elif ch==4:
        eid = int(input('Enter employeee id to delete :'))
        m1.deleteId(eid)
    elif ch ==5:
        break
