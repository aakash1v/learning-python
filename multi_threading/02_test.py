'''Advantages
 Improve performance of the system or application
 Teduce response time of website/application.
 Normal program - 1 flow
 program with n threads - n flows'''

# application - 
# 1. video games eg - pubg
# 2. Multi-media graphics .
# 3. Animations
# 4. Web servers 
# 5. application (To reduce execution time)

# Q. How to achieve threading in python? 
# -By using threading module

# Main thread is created by PVM (interpreter)

# thread are python objects of threading.Thread() class. 

# current_thread()
import threading

print(threading.current_thread())
print(threading.current_thread().name)
print(threading.current_thread().ident)
print(threading.current_thread().is_alive())





