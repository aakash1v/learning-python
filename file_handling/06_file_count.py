#Count lines, words, characters from file.......

import os 
import sys

try:
    str = input('Enter file name: ')
    if(os.path.isfile('/home/aakash/Desktop/'+str)):
        f= open('/home/aakash/Desktop/'+str,'r')
        if(f.readable()):
            mylist =f.readlines()
            wc =lc = cc = 0
            #calculting
            for line in mylist:
                lc +=1
                words = line.split() #split the string into array
                wc = wc + len(words)
                cc =cc+len(line)
            print("Total lines : ",lc)
            print("Total words : ",wc)
            print("Total character : ",cc)
    else:
        print('File not found....')

except Exception as e:
    print(e)