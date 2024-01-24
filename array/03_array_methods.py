import array as arr

myarr = arr.array('i',[10,20,30,20,20,40,50])

myarr.insert(9,0)  #index out of range add the data at the end...
print(myarr)
#this will reverse the array..
myarr.reverse()
print(myarr)


c = myarr.count(20)
print('No of 20 in this array : ',c)

print(myarr)
print('Befor remove ',len(myarr))
myarr.remove(10)
print('After remove ',len(myarr))
print(myarr)

# index 
print(myarr.index(0))
#checking
#checking