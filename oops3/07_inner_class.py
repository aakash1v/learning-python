'''
class TestOuter:
    def __init__(self):
        print('Constructor of Outer')
    
    class TestInner:
        def __init__(self):
            print('Counstructor of Inner')

        def display(self):
            print('Nothing to display ...')
# calling

T1 = TestOuter()
# T2 = TestInner() --with the help of object of outer class we create object of inner class
Ti = T1.TestInner() # -- it will work ... 
#  Ti = object of inner class
Ti.display()
TestOuter.TestInner.display()  #this is an another way....
'''
class Country:
    def __init__(self) :
        print('This is Country class constructor')
    def displayCountry(self):
        print('This is Display method of Country class')
    class State:
        def __init__(self):
            print('This is state class constructor')
        def displayState(self):
            print('This is Display method of State')

        class City:
            def __init__(self):
                print('This is city class constructor')
            def displayCity(self):
                print('This is Display method of city')

C1 = Country()  #instance of country class
C1.displayCountry()
s1 = C1.State() #Instance of State class
s1.displayState()
c1 = s1.City()  #Instance of City class
c1.displayCity()

#Annonymous object -- we can call any method by annonymous object....
#Annonymous obj - object without any name...
Country().displayCountry()
Country().State().City().displayCity() 
