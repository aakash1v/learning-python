#factorial of number using recursion

def factorial(x):
    if x ==0 or x ==1:
        return 1
    else:
        return x*factorial(x-1)


# reverse of number using recursion

s =0 
def reverse(n):
    global s
    if n>0 :
        r = n%10
        s = s*10 + r
        n = n//10
        reverse(n)
    return s



print('Enter a number : ')
n = int(input())
result = reverse(n)
print("reverse no  is %d"%result)
if n==s:
    print("number is palindromer")
else:
    print("numbe is not palindrome")
