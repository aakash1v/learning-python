# Attribute of array in python 
'''
ar.ndim 
ar.shape
ar.size
ar.itemsize
ar.dtype
ar.nbyte
'''
import numpy as np 
myar1 = np.array([1,2,3,4,5])
# [] - subscript 
myar2 = np.array([[1,2,3],[4,5,6]])
print(myar1.ndim,'D')
print(myar2.ndim,'D')

# //shape attribute 
print(myar1.shape)
print(myar2.shape)

# siZe 
print(myar1.size)
print(myar2.size)

# itemsize 
print(myar2.itemsize)

# dtype 
print(myar2.dtype)

# nbyte 
print(myar1.nbytes)
print(myar2.nbytes)



