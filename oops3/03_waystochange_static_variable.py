class Test:
    n = 100 #static variable

    def fist(self):     #non -static method
        Test.n += 10
    
    @staticmethod
    def second():    #static method
        Test.n +=10

    @classmethod
    def third(cls):
        cls.n +=10

# calling 
Test.n +=10
t1 = Test()
t1.fist()
Test.second()
t1.third()
print(Test.n)




