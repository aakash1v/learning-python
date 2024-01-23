# Defination of a function 
def display():
    a = 100
    print("local of function ",id(a))
# calling 
a = 500     
print('local of calling module',id(a))
display()
