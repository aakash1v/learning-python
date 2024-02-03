try:
    f =open("/home/aakash/Desktop/try",'a')
    str = input('Enter string :')
    f.write(str)
    print(f.writable()) #True
    print(f.readable()) #False
    """properties....."""
    print(f.name)  #location of file
    print(f.mode)
    print(f.closed)         

except FileNotFoundError as e:
    print(e)
finally:
    f.close()




