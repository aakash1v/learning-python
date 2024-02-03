try:
    f =open("/home/aakash/Desktop/try",'x')
    str = input('Enter string :')
    f.write(str)
    print(f.writable()) #True
    print(f.readable()) #False
     
    f.close()
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)





