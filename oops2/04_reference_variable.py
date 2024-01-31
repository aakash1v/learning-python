class Customer:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

#obj as an argument.. 
def greet(customer):
    print(id(customer))
    if customer.gender.lower() =='male':
        print(f'Hello {customer.name} sir')
    else:
        print(f'Hello {customer.name} mam')

    cust2 = Customer('Ankita','Female')

    return cust2

cust = Customer('Nitish','male')
print(id(cust))
# print(cust.name)
new_cust = greet(cust)
print(new_cust.name)


#class ke objects are also mutable like lists,dict and sets..

