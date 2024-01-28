class instanceCounter(object):
    count =0

    def __init__(self,val):
        self.val = val
        instanceCounter.count +=1

    def set_val(self,newval):
        self.val =newval
    
    def get_val(self):
        return self.val
    
    def get_count(self):
        return instanceCounter.count
    
a = instanceCounter(5)
b = instanceCounter(13)
c = instanceCounter(7)
# c = instanceCounter(7)

for obj in (a,b,c):
    print('val of object: %s ' %(obj.get_val())) #initialized value(5,13,etc.)
    # print('Count: %s'%(obj.get_count()) )   #always 3
    print('Count: %s' % (obj.count) )   #always 3

'''simple class as a list
'''