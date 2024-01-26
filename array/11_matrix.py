'''Concept of matrix in python
diagonal, transpose,max min,sum,prod,sort,addition,subtraction,division,multiplication
'''
import numpy as np 
myar = np.array([[10,5,7],[9,3,5],[11,15,17]])
mt1 = np.matrix(myar)
# print(mt1)
# print(type(mt1))
# 
# print(mt1.diagonal())
# print(mt1.transpose())
# print(mt1.sum())
# print(mt1.max())
# print(mt1.min())
# 
# print(mt1.prod())
# 
# print(mt1)
# mt1.sort()
# print(mt1)
mt2 =np.matrix('1,12,3;4,15,60;12,8,9')
print(mt2)
print('Sorted elements of matrix row wise : ')
print(np.sort(mt2))
print('Sorted elements of matrix column wise : ')
print(np.sort(mt2,0))



