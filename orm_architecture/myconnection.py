import MySQLdb

class connection:
    @staticmethod
    def getConnection():
        con = MySQLdb.Connect(host = 'localhost',user='root',password ='root',database ='dataflair')
        return con