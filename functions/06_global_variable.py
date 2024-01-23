a = 100 #global
#local variable >> global variable..
def one():
    a = 50  #local variable
    print(a)

def two():
    print(a) # a is a global variable
    
def three():
    global a
    a = a+ 10 #error 
    print('global value ', a)

one()
two()
three() 

