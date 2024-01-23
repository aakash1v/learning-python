#fibonacci series -->  1 2 3 5 8 13 21 
a =0
b = 1
def fibonacci(n):
    global a,b
    if(n==0):
        return n
    else:
        c = a+b
        print(c,end=' ')
        a = b
        b = c
        fibonacci(n-1)


n = int(input('ENter the value of n : '))
fibonacci(n)