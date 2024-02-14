import MySQLdb
from MySQLdb import *

try:
    con = MySQLdb.Connect(host='localhost',user='root',password='root',database='dataflair')
    print('Connection success..')
    eid = int(input('Enter employeee id :'))
    ename = input('Enter Emplyee Name :')
    edept= input('Enter department Name :')
    esal = int(input('Enter salary'))
    value = (eid,ename,edept,esal)
    # print(type(value))
    # sql = "insert into employee values(%d,'%s','%s',%d)"
    # cur.execute(sql%value)
    sql = "insert into employee values({},'{}','{}',{})".format(eid,ename,edept,esal)
    cur= con.cursor()
    cur.execute(sql)
    print('REcord inserted ',cur.rowcount)
    con.commit()


except Exception as e:
    print(e)
finally:
    con.close()
    print('Connection closed...')

