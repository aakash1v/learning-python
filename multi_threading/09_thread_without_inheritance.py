import time
from threading import *

def display(str):
    for i in range(1,11):
        print(str,end=" ")
        print(i)
        time.sleep(1)

def show(str):
    for i in range(100,111):
        print(str,end=" ")
        print(i)
        time.sleep(1)

def abc(str):
    for i in range(20,31):
        print(str,end=" ")
        print(i)
        time.sleep(1)

# calling 
T1 = Thread(target=display,args=("First :",) )
T2 = Thread(target=show,args=("Second :",))
T3 = Thread(target=abc,args=("Third :",))

# print(current_thread().getName())
# print(T1.getName())
# print(T2.getName())

# T1.setName('First')
# T2.setName('Second')

# print(T1.getName())
# print(T2.getName())

T1.start()
T2.start()
T3.start()
