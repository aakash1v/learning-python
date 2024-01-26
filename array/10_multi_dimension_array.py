'''Multi Dimension array in python
array(),ones(),zeros(),eye(),reshape()
'''
import numpy as np 

myar1 = np.array([[10,20,30],[40,50,60]])
# print(myar1)
myar1 = np.ones((3,3),int)
myar1 = np.eye(3) #need size only .. identity matrix

myar1 = np.array([1,2,3,4,5,6,7,8,9])
# myar2= np.reshape(myar1,(3,3))
# or 
myar2 = myar1.reshape(3,3)
print(myar2)




# print(myar1)
