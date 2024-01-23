'''
Types of arguments --
1. actual & formal argument
2. positional argument  -- no of actual arg == no of formal arg...
3. keyword argument
4. default argument
5. variable length argument (var-args)
'''
def display(a,b):    #formal argument
    c = a+b
    print(c)

# calling
a = 100
b = 50
display(a,b)    #actual argument

def stud_info(rollno,name,course):
    print("Roll no is ",rollno)
    print("Name  is ",name)
    print("Course is ",course)


# calling 
stud_info(101,'vinit','B-tech')
stud_info(rollno=102,name='Aquaman',course='Btech')     #keyword argument

def addition(a,b,c,d=0):    #default argument 
    z = a+b+c+d
    print("addition is ",z)

# calling 
addition(10,20,30)


def addition(n,*args):  #var-args
    sum =0
    for m in args:
        sum = sum + m
    print('Total is ',sum)

addition(5,1,2,3,4,5,6)
