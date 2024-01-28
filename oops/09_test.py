from assignments import MaxSizeList


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('Hey')
a.push('Hey')
a.push('Hi')
a.push('Hi')

b.push("let's ")
b.push("let's ")
b.push('go')
b.push('go')

print(a.get_list())
print(b.get_list())
