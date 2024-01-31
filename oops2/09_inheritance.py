""" DRY - Don't Repeat your self 
Inheritance--

Data member
mehtod function
constructor

**private member are not inherited
"""
class User:

    def login(self):
        print('login')
    
    def registor(self):
        print('Registor')

class Student(User):

    def enroll(self):
        print('Enroll')

    def review(self):
        print('Review')

stu1 = Student()
stu1.enroll()
stu1.review()
stu1.login()
stu1.registor()

