from threading import *
import time
def printdata(n):

    print(current_thread().getName()+" Starts here")
    for i in range(1,n+1):
        print(i)
        time.sleep(1)

#main thread
print(current_thread().getName() +"Starts...........")
T1 = Thread(target=printdata,args=(5,),name="First thread")
T2 = Thread(target=printdata,args=(10,),name="Second thread")

print(T1.is_alive()) #True
print(T2.is_alive()) #True

T1.start()
T2.start()

T1.join()
T2.join()

print(T1.is_alive()) #True
print(T2.is_alive()) #True
print(current_thread().getName()+"Ends Here.........")

#Default Join
