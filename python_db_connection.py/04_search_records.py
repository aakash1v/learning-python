import MySQLdb

try:
    con = MySQLdb.Connect(host= 'localhost',user= 'root',password= 'root',database = 'dataflair')
    print('Connection success...')
    sql = "Select * from employee "
    cur = con.cursor()
    cur.execute(sql)
    print('emp_id   ||  emp_name  ||   emp_depart   || emp_salary')
    print('........................................')
    result = cur.fetchall()
    for row in result:
        print("%d  ||    %s        ||     %s    ||   %d"%(row[0],row[1],row[2],row[3]))
        print('................................................')

    
    

except Exception as e:
    print(e)
    
finally:
    con.close()
    print('Connection is closed...')
