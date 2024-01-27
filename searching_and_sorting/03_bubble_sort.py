import array as ar 
myar = ar.array('i',[])

n = int(input('Ente limit : '))
print('Enter elements in array :')
for i in range(n):
    x = int(input())
    myar.append(x)

for i in range(n):
    for j in range (n-i-1):
        if(myar[j]>myar[j+1]):
            myar[j],myar[j+1] = myar[j+1],myar[j]
            # temp = myar[j]
            # myar[j]=myar[j+1]
            # myar[j]=temp
        
print('Sorted array is ',(myar))