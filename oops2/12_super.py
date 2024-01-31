
class Phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ')
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone ')

class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)  #should be first statement inside ..
        self.os = os
        self.ram = ram
        #inside smartphone constructor

    def buy(self):
        print('Buying a smartphone')
        #invoking parent method
        super().buy()

s = SmartPhone(20000,'Samsung',12,'Android',2)
# s.buy()
print(s.os)
print(s.brand)


