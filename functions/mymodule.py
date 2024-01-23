def factorial(n):
    f=1
    while(n!=0):
        f = f*n
        n = n-1
    # print('Factorial is %d'%f)
    return (f)

def reversenum(n):
    s = 0
    while n!=0:
        r=n%10
        s = s*10 + r
        n = n//10
    # print("Reverse of the number is %d "%s)
    return s
 
def area(r):
    a= 3.14*r*r
    return a

def asmd(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return (a,b,c,d)

    
