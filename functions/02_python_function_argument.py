# Defination of a function 
def display():
    a = 100
    print("local of function ",id(a))
# calling 
a = 500     
print('local of calling module',id(a))
display()

# Types of argument 
def addition(*args):
    sum =0
    for i in args:
        sum = sum + i
    print("Sum is  : ",sum)

addition (10,20,30,40)
addition (10,20,30,40,50,60,70)
