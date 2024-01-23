# anonymous - a function without a name
#lambda function

# lambda a,b : statement
# lambda arguments : statements ...

add = lambda a,b : a+b
sub = lambda a,b : a-b
mult = lambda a,b : a*b
div = lambda a,b : a//b
f = lambda x: x**2
#question is how to use it ...
greater = lambda x,y: x if x>y else y

#calling ...
# a = int(input('Enter first number : '))
# b = int(input('Enter second number : '))
# result = add(a,b)

# n = int(input('Enter a number : '))
# result = f(n)
# print(result)
a = 50
b = 10
print("Result is %d"%add(a,b))
print("Result is %d"%sub(a,b))
print("Result is %d"%mult(a,b))
print("Result is %d"%div(a,b))
print("Greater no  is %d"%greater(a,b))
