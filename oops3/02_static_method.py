class Student:
    def __init__(self):
        self.rno = 100
        self.name = 'Rahul'
        self.clgname = 'Data Flair'

    def display(self):
        print(self.rno)
        print(self.name)
        print(self.clgname)

    @staticmethod
    def addition(x,y):
        print(x+y)

#also called utility method...
Student.addition(4,5)

