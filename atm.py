class ATM:
    def __init__(self):
        self.pin=""
        self.balance=0
        
        self.menu()
        
    def menu(self):
        user_input=input("""
        Enter 1 to create pin:
        Enter 2 to Deposite:
        Enter 3 to Withdraw:
        Enter 4 to check balance:
        Enter 5 to exit:""")
        
        if user_input=="1":
            self.createPin()
        elif user_input=="2":
            self.Deposite()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("exit")
        
    def createPin(self):
        self.pin=input("Enter pin: ")
        print("Pin creted successfully")
        self.menu()
    def Deposite(self):
        temp=input("Enter pin:")
        if temp==self.pin:
            amt=int(input("Enter Amount to deposite: "))
            self.balance=self.balance+amt
        else:
            print("Invalid pin")
        self.menu()
    def withdraw(self):
        temp=input("Enter pin:")
        if temp==self.pin:
            amt=int(input("Enter Amount to withdraw: "))
            if amt<self.balance:
                self.balance=self.balance-amt
            else:
                print("Insufficient Amount")
        else:
            print("Invalid pin")
        self.menu()
    def check_balance(self):
        temp=input("Enter pin:")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
        self.menu()
sbi=ATM()


        
                
        
        