'''
Relationship -
1. Aggregation (Has -A)         2. Inheritance (Is- A)
eg-
Customer HAS A address .

2.
Product IS A smartphone
Car     IS A Vehical

'''
#Aggregation....

class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.address = address
        self.gender = gender
        self.address = address
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pin,new_state)

class Address:
    
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state


add = Address('Kolkata',811202,'WB')
#passing address as object...
cust = Customer('Nitish','Male',add)

print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)

cust.edit_profile('Ankit','Gurgao',122011,'Haryana')
print(cust.name)
print(cust.address.state)