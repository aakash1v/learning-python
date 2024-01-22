myset   = set({})
n = int(input("Enter the limit"))
print("Enter element in set")
for i in range(n):
    x = int(input())
    myset.add(x)

print(sum(myset))
