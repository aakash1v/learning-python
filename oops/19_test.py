# Decorators : Class and Static Methods 

class instanceCounter(object):
    count =0

    def __init__(self,val):
        self.val = self.filterint(val)
        instanceCounter.count +=1

    @staticmethod
    def filterint(value):
        if not isinstance(value,int):
            return 0
        else:
            return value
            
a = instanceCounter(5)
b = instanceCounter(13)
c = instanceCounter('hello')

print(a.val)
print(b.val)
print(c.val)
