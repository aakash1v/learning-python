
''' 
object.attribute lookup hierarchy
1. instance
2. the class 
3. Any class from which this class inherits'''

class Date(object):
    def get_date(self): #inherits from the 'object' class
        return '2014-10-13'

class Time(Date):   #inherits from the 'Date' class
    def get_time(self):
        return '10:00:02'

dt =Date()
print(dt.get_date())

tm =Time()
print(tm.get_time())
print(tm.get_date())    #found this method in the 'Date' class

