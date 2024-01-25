# functions of numpy module 

import numpy as np 
myar = np.array([100,200,300,400,500])
new_arr= np.sqrt(myar)
print(new_arr)

arr_sum = np.sum(myar)
print('sum of element is ',arr_sum)

arr_procuct = np.prod(myar)
print("Product of element of array is",arr_procuct)


n = np.min(myar)
p = np.argmin(myar)
print('minmum element is : ',n)
print('index of minimum element is : ',p)

myar = np.array([1,2,3,4,4,4,2,1,9])
newar = np.unique(myar)
print(newar)

a1 = np.array([90,60,120,90])
sin_array = np.sin(a1)
print(sin_array)

print(np.mean(a1))
print(np.median(a1))
sorted_array = np.sort(a1)
print(sorted_array)
print(a1)



