'''Race condition is solved by synchronization --
1. using locks
2. using semaphores
'''

"""
1) Lock class
a. Acquire()
b. Release()

"""
from threading import *
import time

l =Lock()
def printtable(n):
    l.acquire()
    for i in range(1,11):
        print(n*i)
        time.sleep(1)
    l.release()
    
#calling ---
t1 = Thread(target=printtable,args=(5,))
t2 = Thread(target=printtable,args=(9,))
t3 = Thread(target=printtable,args=(7,))

t1.start()
t2.start()
 
t1.join() 
t2.join()

