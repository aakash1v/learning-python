def factorial(n):
    f=1
    while(n!=0):
        f = f*n
        n = n-1
    print('Factorial is %d'%f)

def reversenum(n):
    s = 0
    while n!=0:
        r=n%10
        s = s*10 + r
        n = n//10
    print("Reverse of the number is %d "%s)
 