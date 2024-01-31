''' 
Polymorphism --
1. Method Overriding
2. Method Overloading
3. Operator Overloading'''


class Phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor..')
        self.price = price
        self.__brand = brand
        self.camera = camera
    
    def buy(self):
        print('Buying a phone')

class SmartPhone(Phone):
    def buy(self):
        #method overriding
        print('Buying a smartphone')

s = SmartPhone(30000,'Infinix',8)
# print(s.__brand)
s.buy()
