#serilizing - changing object to byte stream

import pickle,student
try:
    f=open('/home/aakash/Desktop/studentrecord.txt','wb')
    if(f.writable()):
        srno = int(input('Enter roll no :'))
        sname = input('Enter Name  :')
        scourse = input('Enter Course  :')
        S1= student.Student(srno,sname,scourse)

        pickle.dump(S1,f)
        print('File Created...')
        f.close()
except Exception as e:
    print(e)

