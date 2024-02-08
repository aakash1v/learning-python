#Difference between Lock and Rlock
# 2 methods --
# a) acquire
# b) release
#advantange -- multiple times use of acquire and release we should use rlock ...

from threading import *
import time

l = RLock()
def printtable(n):
    l.acquire()
    l.acquire()
    for i in range(1,11):
        print(n*i)
        time.sleep(1)
    l.release()
    l.release()

T1 = Thread(target=printtable,args=(5,))
T2 = Thread(target=printtable,args=(9,))

T1.start()
T2.start()




