class Myclass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def abc(self):
        self.c = 30

m1 = Myclass()
m1.abc()
m1.d = 40
m2 = Myclass()


print('m1 object: ',m1.__dict__)
print('m2 object: ',m2.__dict__)
