#Program for loosely and Tightly couple Application
# INTEFRACE  -- fully abstract class
#1.loosley coupled 
#2. Tighly coupled
from abc import *


#Interface --fully abstract class....
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(Database):
    def connect(self):
        print('Oracle connection success')
    def disconnect(self):
        print('Oracle connection closed')

class Mysql(Database):
    def connect(self):
        print('Mysql connection success')
    def disconnect(self):
        print('Mysql connection closed')

class Sybase(Database):
    def connect(self):
        print('Sybase connection success')
    def disconnect(self):
        print('Sybase connection closed')

#calling

dname = input('Enter Database Name : ')
#changing string into class..
cname = globals()[dname]
D1 = cname()
D1.connect()
print('Database insert')
print('Database search')
print('Database Delete')
print('Database Update')
D1.disconnect()
