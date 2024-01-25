import numpy as np

myar1 = np.array([5,2,11,6,3])
myar2 = np.array([5,2,1,6,3])

# myar3 = (myar1==myar2)
myar3 = (myar1>myar2)
print(myar3)


if (all(myar3)):
    print('hello')
else:
    print('bye')

print('any one is  true') if (np.any(myar3)) else print('no...')

#where
newar= np.where(myar1 %2==0,myar1,0)
print(newar)

myar = np.arange(1,11,1)

#additionof 5 in each element of array
new_arr = myar+5
print(new_arr)

