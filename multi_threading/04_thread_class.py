from threading import *
class MyThread1(Thread):
    def run(self):
        print('This is my Thread1')

class MyThread2(Thread):
    def run(self):
        print("This is myThread2")

# calling
print('Main thread start.....')
t1 = MyThread1()
t2 = MyThread2gity()
t1.start()
t2.start()

print('\nMain thread End......')
