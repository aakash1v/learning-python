class Customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'I am {self.name} and my age is {self.age}.')
    
c1  = Customer('Nitish',34)
c2  = Customer('Ankit',43)
c3  = Customer('Neha',24)


for i in (c1,c2,c3):
    # print(i.name,i.age)
    i.intro()



