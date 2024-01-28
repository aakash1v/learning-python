# try:
#     a= int(input('Enter the number'))
#     b= int(input('Enter the number'))
#     c = a//b
#     print('Division is',c)
# except ZeroDivisionError as e:
#     print('Can not divide by zero')

# except ValueError as e:
#     print('Enter numbers only')

mylist = [10,20,39,40,'hello']
try:
    i = int(input('Enter index number : '))
    b = int(input('Enter a number'))
    print(mylist[i]/b)
except ValueError as e:
    # print('Enter numbers only')
    print(e)

except IndexError as e:
    # print('Invalid index number...')
    print(e)

except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

    


