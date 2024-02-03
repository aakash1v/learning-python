import os,sys

try:
    if (os.path.isfile('/home/aakash/Desktop/try')):
        f = open('/home/aakash/Desktop/try','r')
        count = 0
        sp =0
        dg =0
        while True:
            ch = f.read(1)
            if not ch: # read all character(one by one ) of file....
                break
            # if (ch=='a' or ch =='e' or ch == 'i'or ch=='o'or ch == 'u'):
            #     count +=1

            # # elif(ch==' '):
            # elif(ch.isspace()):
            #     sp +=1
            
            if(ch.isdigit()):
                dg +=1

except Exception as e:
    print(e)
finally:
    f.close()

# print('Total vowel',count)
# print('Total space',sp)
print('Total digit',dg)


