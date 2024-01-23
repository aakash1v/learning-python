import mymodule as my
import math

# n = int(input('Enter a number : '))
# my.factorial(n)

# n = int(input("Enter the number to reverse : "))
# my.reversenum(n)


# print(math.sqrt(6))

n = int(input("Enter a number : "))
x =my.factorial(n)
print('Factorial is %d'%x)


x = my.area(12)
print("Area is %.2f"%x)

a,b,c,d = my.asmd(100,50)
print('Addition is ',a)
print('Substraction is ',b)
print('Multiplication is ',c)
print('Division is ',d)
