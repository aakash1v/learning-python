import time

def printtable(n):
    for i in range(1,11):
        print(f"{n}x{i}= {n*i}")
        time.sleep(1)

def printsquare():
    for i in range(1,11):
        print("{}^2 = {}".format(i,i**2))
        time.sleep(1)

#calling...
start = time.time()

# printsquare()
# printtable(5)

end = time.time()
n = end -start
print("Total time is : %.2f "%n)