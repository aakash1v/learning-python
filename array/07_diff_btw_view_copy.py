import numpy as np 

myar = np.arange(1,11,1)
'''print('My array   : ',myar)

ar = myar
print('Reference Ar',ar)

#change
ar[3]= 100
myar[0] =0  
#after change ..
print('My array : ',myar)
print('Reference Ar',ar)

# id 
print('id of myarrary  ',id(myar))
print('id of reference ',id(ar))
'''
# ar = myar.view()
# # id is different but it is a mirror image change will occure in both..
# print('id of myarrary  ',id(myar))
# print('id of reference ',id(ar))

# myar[2] = 100
# #after change...
# print('Elements of myarray ',myar)
# print('Elements of view  ',ar)

ar = myar.copy()
# id is different and element is also different... 
print('id of myarrary  ',id(myar))
print('id of reference ',id(ar))

myar[2] = 100
#after change...
print('Elements of myarray ',myar)
print('Elements of copied array  ',ar)