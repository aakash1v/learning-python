class Myclass:
    def __init__(self,n):
        self.n = n

    #overloading >
    def __gt__(self,other):
        if (self.n>other.n):
            return True
        else:
            return False
        
    #overloading >=
    def __ge__(self,other):
        if (self.n>=other.n):
            return True
        else:
            return False
        
    #overloading <
    def __lt__(self,other):
        if (self.n<other.n):
            return True
        else:
            return False

    #overloading <=
    def __le__(self,other):
        if (self.n<=other.n):
            return True
        else:
            return False
    
    #overloading ==
    def __eq__(self,other):
        if (self.n==other.n):
            return True
        else:
            return False

# a= int(input('Enter 1st no : '))
# b= int(input('Enter 2nd no :'))
# m1 = Myclass(a)
# m2 = Myclass(b)

# if (m1>m2):  #__gt__(self,other)
#     print('Greate no is first')
# else:
#     print('Greater no is second')


m1 = Myclass(5)
m2 = Myclass(5)
print('value are equal ') if m1 == m2 else print('value are not same')

