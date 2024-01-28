class FiveDivisionError(Exception):
    pass


a = int(input('Enter a number '))
b = int(input('Enter a number '))
try:
    if(b==5):
        # raise ZeroDivisionError('Divide by 5 error')
        raise FiveDivisionError('Divide by 5 error')
    c = a//b
    print('Division is',c)

# except ZeroDivisionError as msg:
#     print(msg)
# except FiveDivisionError as msg:
#     print(msg)
except Exception as e:
    print(e)

    