# Binary search in Python 
import array as ar 
import numpy as np 
n = int(input('Enter the limit : '))
myar = ar.array('i',[])

print('Enter %d elements in Array '%n)
for i in range(n):
    x = int(input())
    myar.append(x)

s = int(input('Enter an element for search : '))

# if s in myar:
    # print('Searching success ')
# else:
    # print('Searching not success')

myar1 = np.reshape(myar,(n))
myar1.sort()

low =0
high = n-1
f=0
while(low<=high):
    mid= (low+high)//2
    if(s==myar1[mid]):
        f=1
        break
    elif(s>myar1[mid]):
        low=mid+1
    else:
        high = mid-1

if(f==0):
    print('searching not success')
else:
    print('searching success')
