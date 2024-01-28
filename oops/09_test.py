from assignments import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('Hey')
a.push("let's ")
a.push('Hi')
a.push('go')

b.push('Hey')
b.push("let's ")
b.push('Hi')
b.push('go')

print(a.get_list())
print(b.get_list())
