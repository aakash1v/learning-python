'''Program for Create Matrix using runtime element'''
import numpy as np
import array as ar 

# m,n = map(int,input().split())
# print(m,n)

m,n = [int(a) for a in input('Enter values of row and column ').split()]
print(m,n)

myar1 = ar.array('i',[])
x = m*n
print('Enter %d elements in matrix : '%x)
for i in range(x):
    var = int(input())
    myar1.append(var)


print(myar1)

myar2 = np.reshape(myar1,(m,n))
# print(myar2) 

mt = np.matrix(myar2)
print(mt)

print(mt.transpose())