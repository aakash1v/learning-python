class Phone:

    def __init__(self,price,brand,camera):
        print("Inside phone constuctor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print('Buying a phone')

class Product:
    def review(self):
        print('Customer review')
    def buy(self):
        print('Product buy method')

class SmartPhone(Product,Phone):
    pass

s = SmartPhone(2000,'Apple',12)

'''MRO - Method resolution order '''
s.buy()
s.review()
