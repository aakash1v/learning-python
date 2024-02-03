import os,sys

try:
    if(os.path.isfile('/home/aakash/Desktop/try')):
        with open('/home/aakash/Desktop/try','r') as f:
            for line in f:
                print(line)
    else:
        print('File not found ')
except Exception as e:
    print(e)