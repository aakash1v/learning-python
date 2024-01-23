# filter function with lambda expression 

# mylist = [10,7,8,12,66,33,67]
# mylist1 = list(filter(lambda x:x%2==0,mylist))
# print(mylist1)

mystr = 'Data Flair'

str1 = list(filter(lambda x: x in ['a','e','i','o','u'],mystr))
print(str1)

