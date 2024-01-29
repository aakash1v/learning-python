# Use of Self variable in python  

class Test:
    def __init__(self):
        #implicit callling of constructor..
        # print('This is init method of class')
        self.rno = 101
        self.name = 'Aakash'
        self.clgname ='Sandip University'
            
    def __str__(self):
        # return 'Data Flair Indore'
        str = "Roll no = {}\nName \t= {}\nCollege name = {}".format(self.rno,self.name,self.clgname)
        return str

#implicit calling of str & init...
T1 = Test()
print(T1) 

