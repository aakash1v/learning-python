#exception handling program ....


try:
    a = int(input('Enter a number '))
    b = 7/a
    print(b)

# use specific error is a good practice..
# u can so many error 

except ZeroDivisionError as e:
    print('This is wrong input : ',e)

except ValueError as e:
    print('This is wrong input : ',e)

except Exception as e :
    # Exception is a super class
    print('This is a wrong input :',e)
    
finally:
    print('This will be executed always..')

# list =[2,3,4,5,6,7]
# for i in list:
    # print(i,end=' ')

