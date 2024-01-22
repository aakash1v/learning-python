"""
[]  - list
()  - tuple
{}  -set   /forzen set/ Dictionary
"""
# set is mutable 
# inserting order in preserved
# Duplicate not allowed     --it is useful
# Not access with index number  --it will create error
# Slicing not allowed

# {}  - set/ frozen set /dictionary 
myset = {}
# print(type(myset))  #dictionary by default

# myset   = {2}
# myset   =set({})

# print(type(myset))  #now it is set

# myset   =frozenset({})
# print(type(myset))

# myset   = set({})
# n = int(input("Enter the limit"))
# for i in range(n):
#     x = input()
#     myset.add(x)

# for x in myset:
#     print(x,end=" ")

myset= {10,20,30,30,40,800}
# print(myset)
myset.add(100)
# myset.discard(10)
# myset.remove(1000)  #error if not exist before
# myset.pop()     #delete the value inserted at last
myset2 =myset.copy()

print(myset2)
for x in myset:
    print(x,end=" ")

myset1 = {10,100,0,1}
print(myset1.union(myset2))
myset1.clear()
print('\n',myset1)

