#Exception in Multithreading......
import time
from threading import *
import threading

def my_hook(args):
    print("****** My except hook method ******")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def fun1():
    print("This is function 1")
    s = "Hello"+10

def fun2(n):
    for i in range(1,n+1):
        print(i*i)
        time.sleep(1)



# calling 
threading.excepthook = my_hook
t1 =Thread(target = fun1,name = 'First')
t2 =Thread(target = fun2,args=(10,),name = 'Second')

t1.start()
t2.start()
t1.join()
t2.join()


# sys.excephook() - default handler when exception arise in  main

#threadin.excephook() - for thread

"""
1. Exception class name
2. message
3. Trace ball detail -(line no)
4.Thread name
"""



 