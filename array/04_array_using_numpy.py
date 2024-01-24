'''
Array creation using Numpy in python
1. using array() function
2. using linespace() function
3. using arrange() function
4. using zeros() function
5. using ones() function

'''
import numpy as np 
myar = np.array([10,5,7,9,45],int) #u can skip int because it is by default int
print(myar)
print(type(myar))

for x in myar:
    print(x,end=' ')

# 2. using linespace()
myar = np.linspace(0,10,5) #create equal book..
print(myar)

# 3. using arange() function 
start= 1
stop = 10
step = 2
myarr = np.arange(start,stop,step)
print(myarr)

new_arr = np.arange(10,0,-1)
print(new_arr)

# 4. using zeroes function 
myar = np.zeros(3)
print(myar)

# 5. using ones function 
myar= np.ones(10,int)
print(myar)


