import array as ar 
import numpy as np 

myar = ar.array('i',[])
n = int(input('Enter the limit : '))

print('Enter elements : ')
for i in range(n):
    x = int(input())
    myar.append(x)

#we need to sort the array .... first..
a= np.sort(myar)


F= 0
s = int(int(input('Enter an element for search : '))) 
low =0
high = n-1
while(low<=high):
    mid = (low +high)//2

    if(s==a[mid]):
        F =1
        break
    elif(s>a[mid]):
        low = mid+1
    else:
        high = mid-1

if(F==1):
    print('Searching success ')
else:
    print('searching not success ')
print(myar)
print(a)