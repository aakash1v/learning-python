# program for create matrix using runtime element by string 

import numpy as np 

m,n = map(int, input('Enter the value of row and column : ').split())
x = m*n
str= input('Enter %d elements : '%x)
print(str)

mt =np.reshape(np.matrix(str),(m,n))

print(mt)

