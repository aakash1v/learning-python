#How many ways we use static variable
class Test:
    n = 100

    def __init__(self):   #constructor
        Test.n += 10

    def nonstaticmethod(self): # non-static method
        Test.n = Test.n + 10

    @staticmethod
    def mystaticmethod(self): #Static method
        Test.n +=10
    
    @classmethod
    def myclassmethod(cls): #class method
        cls.n +=10

#calling 
t1 = Test()
t1.nonstaticmethod()

Test.n +=10 #use static outside the class...
print(Test.n)


