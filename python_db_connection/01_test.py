import MySQLdb
from MySQLdb import *
try:
    con = MySQLdb.connect(host='localhost',user='root',password='root',database= 'dataflair')
    print('Connection successfully......')
    sql = "insert into employee values(113,'damn' ,'cool',80000)"
    cur = con.cursor() #creating a cursor object.......
    cur.execute(sql)  #inserting a record in table employeee..
    print('Record inserted....',cur.rowcount) #but not saved yet...
    con.commit()  #changes saved.....  
    # con.close()
except Exception as e:
    print(e)
finally:
    con.close()
    print('Connection closed.....')


    

