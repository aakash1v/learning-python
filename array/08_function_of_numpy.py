''' 
numpy function..
sqrt,power,sum,prod,max ,min,sin,cos,tan,log,argmin,argmax,unique,concate
abs,mean,median,var  
'''


import numpy as np 
myar = np.array([125,500,600,20,20,125])
myar1 = np.sqrt(myar)
print(myar1)

a1= np.array([1,2,3,4,5])
a1_power = np.power(a1,3)
# to change existing array 
# myar = np.power(myar,3)
print(a1_power)

a1_sum = np.sum(a1)
a1_product = np.product(a1)
print('sum and product of array is ',a1_sum,'and',a1_product)

maximum= np.max(a1)
position_max = np.argmax(a1)
print('max is ',maximum,'and position is ',position_max)

# similar for - min argmin 

sin_array = np.sin(a1)
print(sin_array)

my_unique_array = np.unique(myar)
print(my_unique_array)

