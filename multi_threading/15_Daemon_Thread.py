"""from threading import *
import time 

def table(n):
    for i in range(1,11):
        print(n*i)
        time.sleep(1)


#calling main....
print(current_thread().isDaemon())
# current_thread().setDaemon(True) -- this is not allowed...
T1 = Thread(target=table,args=(5,),name="First thread")
T1.setDaemon(True)  #now thread is running in background....
T1.start()
# print(current_thread().isDaemon())
"""

from threading import *
import time

def first():
    print("This is first function")
    T2 = Thread(target=second)
    print(T2.isDaemon())

def second():
    print("This is second function")

#main calling.....
T1 = Thread(target=first)
T1.setDaemon(True)
T1.start()
print(T1.isDaemon())
