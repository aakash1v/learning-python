import MySQLdb

try:
    con = MySQLdb.Connect(host= 'localhost',user= 'root',password= 'root',database = 'dataflair')
    print('Connection success...')
    emp_id = int(input('Enter the value for Employee id to delete :'))
    sql = "Select * from employee where eid =%d"
    cur = con.cursor()
    cur.execute(sql%emp_id)
    row = cur.fetchone()
    if cur.rowcount ==0:
        print('No record found..')
    else:
        print("%d  %s %s %d "%(row[0],row[1],row[2],row[3]))
        if input('Do u really want to delete ??').lower().startswith('y'):
            sql = "delete from employee where eid=%d"
            cur.execute(sql%emp_id)
            con.commit()
            print('Successfully deleted...')

        else:
            print('Thank you...please try again..')
    
    

except Exception as e:
    print(e)

finally:
    con.close()
    print('Connection is closed...')
