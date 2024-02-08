# from threading import *
# import time

# l=Lock()
# class Table:
#     def printtable(self,n):
#         l.acquire()
#         for i in range(1,11):
#             print(n*i)
#             time.sleep(1)
#         l.release()

# class Mythread1(Thread):
#     def run(self):
#         T=Table()
#         T.printtable(5)

# class Mythread2(Thread):
#     def run(self):
#         T =Table()
#         T.printtable(9)

# m1 = Mythread1()
# m2 = Mythread2()

# m1.start()
# m2.start()

# m1.join()
# m2.join()

# object oriented approach

from threading import *
import time

class Table:
    def __init__(self):
        self.l = Lock()
    
    def printtable(self,n):
        self.l.acquire()
        for i in range(1,11):
            print(n*i)
            time.sleep(1)
        self.l.release()

T = Table()
T1 = Thread(target=T.printtable,args=(5,))
T2 = Thread(target=T.printtable,args=(9,))

T1.start()
T2.start()

T1.join()
T2.join()