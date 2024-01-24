import array as arr

# append (push)
myar= arr.array('i',[10,20,30,40,50])
myar.append(100)
print(myar)

# insert the element at index..
myar.insert(0,0)    #displace the already present element at that index
print(myar)

myar.remove(20) #will remove the 1st occurence of 20.
print(myar)

#count
n = myar.count(10)
print('Number of 10 in the array is ',n)
if(n>0):
    print('Searching succes..')
else:
    print('Searching unsuccess..')

# pop 
myar.pop() # 100 will be removed ..
print(myar)

# tolist
mylist = myar.tolist()
mylist.append('Data flair') # u can append anythin now

# tostring 
myarr2 = arr.array('u',['a','m','u','s','e'])
# s = myarr2.tostring()  -- it is not working..

s= ''.join(myarr2[i] for i in range(len(myarr2)) )
print(s)





