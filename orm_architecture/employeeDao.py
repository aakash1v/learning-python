import myconnection as mcon
import model

class EmployeeDao:
    def __init__(self):
        #stablishing connection....
        self.con = mcon.connection.getConnection()
        self.cur = self.con.cursor()
        print('Connection success....')

    def insertEmployee(self,E):
        try:
            sql = "insert into employee value ('%d','%s','%s','%d')"
            value = (E.get_eid(),E.get_ename(),E.get_edept(),E.get_esal())
            self.cur.execute(sql%value)
            self.con.commit()
            print('Record inserted ',self.cur.rowcount)
        except Exception as e:
            print(e)

    def searchEmployee(self,eid):
        try:
            sql = "select * from employee where eid= %d"
            self.cur.execute(sql%eid)
            if (self.cur.rowcount>0):
                result = self.cur.fetchone()
                E = model.Employee()
                E.set_eid(result[0])
                E.set_ename(result[1])
                E.set_edept(result[2])
                E.set_esal(result[3])
                return E
            else:
                E1 = None
                return E1
        except Exception as e:
            print(e)

    def deleteEmployee(self,eid):
        sql = "delete from employee where eid=%d"
        self.cur.execute(sql%eid)
        self.con.commit()

    def updateEmployee(self,E):
        sql =" update employee set ename = '%s',dept='%s',salary=%d where eid = %d; "
        value = (E.get_ename(),E.get_edept(),E.get_esal(),E.get_eid())
        self.cur.execute(sql%value)
        self.con.commit()
        print('Record updated ',self.cur.rowcount)

    def searchAll(self):
        mylist = []
        try:
            sql = "Select * from employee "
            self.cur.execute(sql)
            result = self.cur.fetchall()
            for row in result:
                E = model.Employee()
                E.set_eid(row[0])
                E.set_ename(row[1])
                E.set_edept(row[2])
                E.set_esal(row[3])
                mylist.append(E)
            return mylist


        except Exception as e:
            print(e)

    def __del__(self):
        self.con.close()
        print('Connection Closed...')