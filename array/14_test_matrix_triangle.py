import numpy as np 
import array as ar 

m,n = [ int(a) for a in input('Enter values of row and cloumn :').split() ]
x = m*n

myar1 = ar.array('i',[])
print('Enter %d elements in matrix : '%x)

for i in range(x):
    var = int(input())
    myar1.append(var)


myar2 = np.reshape(myar1,(m,n))
print(myar2)

print('lower triangle of matrix : ')
for r in range(m):
    for c in range(n):
        if r>=c:
            print(myar2[r][c],end = " ")

print('\nupper triangle of matrix : ')
for r in range(m):
    for c in range(n):
        if r<=c:
            print(myar2[r][c],end = " ")

print('\ndiagonal of matrix : ')
for r in range(m):
    for c in range(n):
        if r==c:
            print(myar2[r][c],end = " ")