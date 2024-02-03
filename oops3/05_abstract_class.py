''' Abstact class are those class whose object can not be defined.....
abstract method -- wo method jiski khud ki defination nahi h hama define karna h...

Meta class -- ABC (abstract base class)     [abc module]


'''
from abc import ABC,abstractmethod

class Button(ABC):
    
    @abstractmethod
    def click(self):
        pass
    
    def display(self):
        print('This is display method..')

class MyColor(Button):
    def click(self):
        print('color is red..')

class MyPhoto(Button):

    def click(self):
        print('This is my photo..')

m1 = MyColor()
m2 = MyPhoto()
m1.click()
m2.click()
