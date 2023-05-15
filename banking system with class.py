class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",self.cname,"Your Account",self.acno,
              "Is Opened with Rs.",self.balance)
        
    def deposit(self,amount):
        self.balance+=amount
        print("Amount Deposited Successfully")
       
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            self.needs=amount-self.balance
            print("Sorry you need another ",self.needs," Amount to Withdraw")
    
    def checkBalance(self):
        print("Current Balance : ",self.balance)
        
b1=Bank()
cname=input("Enter Customer Name : ")
acno=int(input("Enter Account Number : "))
balance=int(input("Enter Initial Balance : "))
b1.openAccount(cname,acno,balance)

while True:
    print("*"*40)
    print("1. Deposit")
    print("2. Withdrawal ")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*40)
    choice=int(input("Enter Your Choice :"))
    print("*"*40)

    if choice==1:
        amount=int(input("Enter Deposti Amount :"))
        b1.deposit(amount)
        print("*"*40)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount :"))
        b1.withdraw(amount)
        print("*"*40)
    elif choice==3:
        b1.checkBalance()
        print("*"*40)
    else:
        print("Thankyou for using our services")
        print("*"*40)
        break
        
    
