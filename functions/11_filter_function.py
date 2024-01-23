# syntax 
# filter (function, sequence/collections)   --True/False
# kept data for true value but boycot data for false

mylist = [1,20,30,5,14,9]
check_even = lambda x: True if x%2 ==0  else False

result = filter(check_even,mylist)  #result as a filter object so typecast it ...
print(list(result))

# other option
result = list(filter(lambda x : x%2!=0,mylist))
print(result)

str = 'This is a sentence okay '
vowel = ['a','e','i','o','u']

result = list(filter(lambda x: x in vowel ,str))
print(result)

def prime(n):
    i = 2
    check =1
    while(i<n):
        if n%i ==0:
            check = 0
        i =i+1
        
    if(check ==1) and n is not 1:
        return True
    else:
        return False

result = list(filter(prime,mylist))
print(result)