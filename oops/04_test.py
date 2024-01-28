class Myclass(object):
    #setter method..
    def set_val(self,val):
        self.value = val
    
    #getter method..
    def get_val(self):
        return self.value
    
a= Myclass()
b= Myclass()

a.set_val(10)
b.set_val(100)
#we acces the value in the main body of the code..
a.value = 'hello'

print(a.get_val())
print(b.get_val())
