#Threads for methods

from threading import Thread

class Example:
    # @classmethod
    @staticmethod
    def display(n):
        for i in range(n):
            print("Hello world")

e1 = Example()
t1 = Thread(target=Example.display,args= (5,))
t1.start()
for i in range(5):
    print('Welcome!')

