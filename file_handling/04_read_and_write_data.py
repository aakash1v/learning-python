import os 
import sys

str = input("Enter file ame for read data :")
try:
    if(os.path.isfile('/home/aakash/Desktop/'+str)):
        f = open('/home/aakash/Desktop/'+str,'r')
        
        if(f.readable()):
            text = f.read()
            print(text)

    else:
        print('File not exists')
        sys.exit()
except FileNotFoundError as e:
    print(e)

