from threading import *
import time

class Mythread(Thread):
    def run(self):
        print(current_thread().getName()+' starts')
        for i in range(1,6):
            print(i)
            time.sleep(1)
        print(current_thread().getName()+' finish')

# calling place 
print(current_thread().getName() +' starts')
print()
T1 = Mythread()
T2 = Mythread()
T1.start()
T2.start()

print(T1.is_alive())
print(T2.is_alive())

T1.join()
T2.join()

print(T1.is_alive())
print(T2.is_alive())

print(current_thread().getName() +' finish')

