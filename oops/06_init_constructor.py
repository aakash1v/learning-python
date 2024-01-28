class MyNum(object):
    def __init__(self,value):
        print('calling __init__ ..')
        try:
            value = int(value)
        except ValueError:
            value =0

        self.val =value
    
    def increment(self):
        self.val = self.val +1

dd = MyNum(5)   #calling __init__
dd = MyNum('hello')   #calling __init__

dd.increment()
dd.increment()  # +2

print(dd.val)

