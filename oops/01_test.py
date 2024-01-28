'''
Class: a blueprint for an instance
Instance: a constructed object of the class
Type: indicates the class the instance belongs to 
Attribute: any object value: object.attribute
Method: a "collable attribute" defined in the class  
'''
var = 'hello,word!'
# print(type(var))
# print(var.upper())

class Myclass(object):
    var = 10

this_obj = Myclass()
that_obj = Myclass()

print(this_obj.var)
print(that_obj.var)

#An instance of a class knows that class it's from vars defined in the class are available to the instance
#attribute is located in the class 
