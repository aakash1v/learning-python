import pickle,student
import os
try:
    str = '/home/aakash/Desktop/studentrecord.txt'
    if(os.path.isfile(str)):
        f = open(str,'rb')
        if(f.readable()):
            s = pickle.load(f)
            # s.display()
            print(s)

    f.close()
except Exception as e:
    print(e)

