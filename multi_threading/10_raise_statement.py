
try:
    a = int(input("Enter first No :"))
    b = int(input("Enter second No :"))
    
    
    if(b==5):
        raise ZeroDivisionError("Divide by zero error ...") #Customize  zero division error msg..
    c = a//(5-b)
    print("Division is ",c)
    
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

