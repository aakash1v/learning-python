''' There are two ways to creating threads :-
1. Using thread class present in threading module.
2. By extending Thread class
'''
from threading import Thread , current_thread

#Create a function containing code to be executed parallely
def display(n,msg):
    print('t1 thread details ',current_thread())
    for i in range(n):
        print(msg)

#creating new thread Here
t1 = Thread(target=display,args=(4,'Hello')) #arguments passes as tuple.. (,) u can also uses key-word argument
#start the new thread
t1.start()
for i in range(4):
    print('welcome')