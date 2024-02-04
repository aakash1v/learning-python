import time
from threading import *

def display():
    for i in range(1,11):
        print(i)
        time.sleep(1)
    
def show():
    for i in range(100,111):
        print(i)
        time.sleep(1)


# calling place     -- main thread
start = time.time() #current time
''' 
display1()
show()
'''
#new born state
t1 = Thread(target=display) #for arguments agrs = (first,second...)
t2 = Thread(target=show)

#runnable state
t1.start()
t2.start()
#DEFAULT JOIN MODE-
#jab apki thread execution karti h or main thread ka execution termination pa aa jata h to main halt ma wait karti ha
#jabta t1,t2 apna execution complete nahi kar lati h
#or ye t1, or t2 default join mode ma execution karti hh...
#implict join mode..

print(t1.getName()) #thread1(show)
print(t2.getName()) #thread2(display)
t1.is_alive() #to check thread is alive or not
t1.setName('One ') #u can change the name of thread like this ....


end = time.time() #this is not working... what should i do..
print(end-start)


