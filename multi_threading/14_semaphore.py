from threading import *
import time


s = Semaphore(3)
def displaydata():
    s.acquire()
    for i in range(1,11):
        print(current_thread().getName() ,i)
        time.sleep(1)
    s.release()

#main...
T1 = Thread(target=displaydata, name='First' )
T2 = Thread(target=displaydata, name='Second')
T3 = Thread(target=displaydata, name='Third')
T4 = Thread(target=displaydata, name='four')
T5 = Thread(target=displaydata, name='five')
T6 = Thread(target=displaydata, name='six')

T1.start()
T2.start()
T3.start()
T4.start()
T5.start()
T6.start()

