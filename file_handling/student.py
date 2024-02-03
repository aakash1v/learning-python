class Student:
    def __init__(self,rno,name,course):
        self.rno = rno
        self.name = name
        self.course=course

    def display(self):
        print('Roll no : ',self.rno)
        print('Name  : ',self.name)
        print('Course : ',self.course)
    
    def __str__(self):
        str = "Roll no={}, Name ={} , Course= {}".format(self.rno,self.name,self.course)
        return(str)
        