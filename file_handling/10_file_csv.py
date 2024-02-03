import csv
try:
    f = open("/home/aakash/Desktop/college.csv",'w',newline='')
    obj = csv.writer(f)

    obj.writerow(['College_id','College Name','Address'])
    print('File...created')
    while True:
        cid = int(input('Enter college Id :'))
        cname = input("Enter college name")
        caddress = input('Enter address :')
        obj.writerow([cid,cname,caddress])

        choice = input('Want to continue ??')
        if (choice.lower() =='no'):
            break
    f.close()
except Exception as e:
    print(e)
