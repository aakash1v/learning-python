import os
import sys

try:
    if(os.path.isfile('/home/aakash/Pictures/Wallpapers/b6.jpg')):
        f1 = open('/home/aakash/Pictures/Wallpapers/b6.jpg','rb')
        f2 = open('/home/aakash/Desktop/new_data1.jpg','wb')
        bytes =  f1.read()
        f2.write(bytes)
        f1.close()
        f2.close()
        print('New file created')

    else:
        print('File not found')
        sys.exit()

except Exception as e:
    print(e)

    