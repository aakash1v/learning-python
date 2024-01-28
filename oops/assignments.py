class MyClass:
   
    def __init__(self):
        self.aa =5
        self.bb ='hello'
        self.cc = ['a','b','c','d']

# myinst = MyClass()                
# print(myinst.cc)

class MaxSizeList:
    def __init__(self,size):
        self.inner_list =[]
        self.max_size = size

    def push(self,obj):
        self.inner_list.append(obj)
        if len(self.inner_list) >self.max_size:
            self.inner_list.pop(0)

        
    def get_list(self):
        return self.inner_list
    
    