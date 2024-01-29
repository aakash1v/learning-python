# Role fo Constructor in inheritance 

class First:
    def __init__(self):
        print('This is constructor of First Class')

class Second(First):
    def __init__(self):
        print('This is a constuctor of Second Class')

# f1 = First()
# s1 = Second()

class Student:
    def __init__(self):
        self.rno = 100
        self.name = 'Aakash Kumar'
        self.course = 'B-Tech'

class Marks(Student):
    def __init__(self):
        self.per = 90


    def display(self):
        print(self.per)
        print('----------')
        print(self.rno)
        print(self.name)
        print(self.course)

M1 = Marks()
M1.display()
