class Atm:

    #constructor
    #special /magic/dunder method

    #instance variable  -- jinka value har object ka liya aalag hoga..
    def __init__(self):
        '''u can hide variables and methods by using double underscore '__'
         __balance = __Atm__balance  (to access)
         --> nothing in python is truly private...
         '''
        self.__pin = ""
        self.__balance = 0

        # print(id(self))
        # self.__menu()

    def set_pin(self,new_pin):
        if type(new_pin) == str:
            self.pin = new_pin
            print('Pin changed')
        else:
            print('Not allowed!')


    def get_pin(self):
        return self.__pin

    def __menu(self):
        user_input=''
        while(user_input !='5'):
            user_input = input("""
         Hello, how would you like to procced??
         1. Enter 1 to create pin
         2. Enter 2 to deposit
         3. Enter 3 to withdraw
         4. Enter to check balance
         5. Enter 5 to exit
         >""")
            if user_input =='1':
                self.create_pin()
            elif user_input =='2':
                self.deposit()
            elif user_input =='3':
                self.withdraw()
            elif user_input =='4':
                self.check_balance()
            else:
                print('Bye Bye...')
    
    def create_pin(self):
        self.__pin = input('Enter your pin :')
        print('Your pin is successfully set...')

    def deposit(self):
        temp = input('Enter your pin :')
        if temp == self.__pin:
            amount = int(input('Enter the amount'))
            self.__balance = self.__balance + amount
            print('Deposit successful')

        else:
            print('Invalid pin!')

    def withdraw(self):
        temp = input('Enter your pin :')
        if temp == self.__pin:
            amount = int(input('Enter the amount'))
            if amount <=self.__balance:
                self.balance = self.__balance - amount
                print('Operation successfully')
            else:
                print('Insufficient balance...')

        else:
            print('Invalid pin!')
    
    def check_balance(self):
        temp = input('Enter your pin :')
        if temp ==self.__pin:
            print('Your current balance is ',self.__balance)
        else:
            print('Invalid pin!')

sbi = Atm()

new_pin= input('Enter your pin :')
sbi.set_pin(new_pin)
print(sbi.get_pin)
# print(id(sbi)) == id(self)
#which means sbi is self..
#currently working object is self 

