class Animal(object):
    #object is build in super class 
    def __init__(self,name):
        self.name =name

    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

class Dog(Animal):
    def fetch(self,thing):
        print('%s goes after the %s!'%(self.name,thing))
    
class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string! '%(self.name))

r=Dog('Rover')
f=Cat('Fluffy')

r.fetch('Paper')    #Rover goes after the paper!
f.swatstring()      #Fluffy shreds the string!
r.eat('dog food')   #Rover is eating dog food.
f.eat('Cat food')   #Fluffy is eating cat food.
r.swatstring()      #AttributeError: 'Dog' object has no attribute 'swatstring'

