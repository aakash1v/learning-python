import os

choice=0
while(choice!=5):
    print('--------------Menu------------------')
    print('1. Notepad\n2. Calculator\n3. Word\n4. Excel\n5. Exit')
    print('-------------------------------------')
    choice= int(input('Enter your choice :'))
    if (choice==1):
        os.system('notepad')
    elif (choice==2):
        os.system('calc')
    elif (choice==3):
        os.system('word')
    elif (choice==4):
        os.system('excel')