from time import sleep
from threading import Thread

videos = ['OOP Syllabus','constructor','destructor','file handling']

class MyClass(Thread):
    def __init__(self,val):
        super().__init__()
        self.kid = val
        print('constructor called')


    def Compression(self):
        print('Video compression code..')

    def run(self):
        self.Compression()
        if self.kid:
            print('Suitable for kid')
        for vid in videos:
            print(f'{vid} started uploading...')
            sleep(2)
            print(f'{vid} uploaded.')
            
        

t1 = MyClass(True)
t1.start()


for i in range(4):
    sleep(0.5)
    print('Checking copyrights')

