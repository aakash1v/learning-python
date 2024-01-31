"""polymorphism
1. method overriding
2. method overloading
3. Operator overloading"""

class Geometry:
    def area(self,radius):
        return 3.14*radius*radius

    #method overloading will not work..
    def area(self,l,b):
        return l*b
    
    #this will override the other area functionss....
    def area(self,a,b=0):
        if b==0:
            print('Circle : ',3.14*a*a)
        else:
            print('Rect : ',a*b)

obj = Geometry()
obj.area(4) 
obj.area(4,5)
