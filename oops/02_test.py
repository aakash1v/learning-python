class Joe(object):
    greeting = 'hello,Joe'
    #the instance is passed as a implicit first argument..
    def callme(self):
        print('calling "callme" method with instance: ')
        print(self)
thisjoe = Joe()

# print(thisjoe.greeting)
thisjoe.callme()
print(thisjoe)

#instance mehtods are variables defined in the class 
#instance is gonna be passed first...(self)




