a = 100
b = 50
def first():
    a = 5
    b = 10
    print('local values ',a,b)
    print('global values ',globals()['a'],globals()['b'])

first()
'''
global - is a  keyword
globals() - is a function
'''