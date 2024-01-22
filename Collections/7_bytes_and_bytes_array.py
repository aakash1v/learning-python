"""" 
1 byte = 8 bit  (0-256)
0 to 255 is only allowed
other number are not allowed

"""
mylist = [2,9,5,255]
mybyte = bytes(mylist)  #it is immutable can't be changed any element
print(type(mybyte))
print(mybyte)



myset =set(mylist)
print(myset)

''' byte_array 
byte array - mutable ...
    can be changed      --it is good :)
'''

mybyte = bytearray(mylist)
print(mybyte)
print(type(mybyte))
mybyte[1]= 100
print(mybyte)
