import array as arr

myar = arr.array('b',[10,20,30,-40,-50,-10,90])   #signed array (-128,127)
print(myar)

myar = arr.array('B',[10,20,30,40,10,190])   #signed array (-0,255)
# Direct access... 
for i in myar:
    print(i,end=' ')

# access data using index number 
for i in range(len(myar)):
    print(myar[i],end=' ')

# slicing of array 
# print(myar[1:4])
print()

newarr = arr.array('i',[])
# print(len(newarr))
n = int(input("Enter the limit : "))
print("ENter elements in array : ")
for i in range(n):
    x = int(input())
    newarr.append(x)

print("Elements of my array : ",end='')
for i in newarr:
    print(i,end=' ')


