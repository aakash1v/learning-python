from threading import *
import time


class MyThread1(Thread):
    def run(self):
        for i in range(10):
            print('This is my Thread1 : ',i)
            time.sleep(1)

class MyThread2(Thread):
    for i in range(10):
            print('This is my Thread2: ',i)
            time.sleep(1)

# calling
print('Main thread start.....')

t1 = MyThread1()
t2 = MyThread2()
t1.start()
t2.start()
start = time.time()

t1.join()
t2.join()
end = time.time()
print(end-start)

print('\nMain thread End......')
