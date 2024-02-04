""" Life Cycle of a thread...
1. New born = jab ham thread banayage
2. runnable state - ready for execution
3. running state    =output yahi milaga..
4. Halt mode/state  --> runnable (queue ma lag jayage in runnable..)
5. DEad

"""
#main thread..
from threading import *
print(current_thread().getName)

"""
Ways to create thread..
1. without using Thread class --(function oriented approach)
2. Inherit your class with thread class
3. without Iherit class with thread class

"""