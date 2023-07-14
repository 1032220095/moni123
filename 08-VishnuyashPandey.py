#08-ITB-Vishnuyash Pandey
class SimpleBankingSystem():
    def __init__(self,deposit,withdraw,CI,balance):
        self.deposit = deposit
        self.withdraw = withdraw
        self.CI = CI
        self.balance = balance

    def Deposit(self,x):
        self.x = x
        self.balance += x
        print(self.balance,"this amount is deposited in your account")

    def Withdraw(self,y):
        self.y = y
        if self.balance-y>0:
            self.balance -= y
            print(y,"this amount is withdrawled from your account")
        else:
            print("Insufficient Balance")
         
    def Balance(self):
        print("Your current balance is :",self.balance)

    def Compound(self,years,roi,amount):
        self.years = years
        self.roi = roi
        self.amount = amount
        print("Your Interest of rate ",roi,"% for ",years," years on a principal of ",amount,"Rs is : ",amount*((1 + roi/100))**years)
        
pepe = SimpleBankingSystem(0,0,0,0)

print("1 : Deposit")
print("2 : withdraw")
print("3 : Balance")
print("4 : Compound Interest")
print("5 : Create Account")

while True:
    n = int(input("Enter Your Choice : "))
    if n==1:
        a = int(input("Enter the amount you want to deposit : "))
        pepe.Deposit(a)
        
    elif n==2:
        b = int(input("Enter the amount you want to withdraw : "))
        pepe.Withdraw(b)

    elif n==3:
        pepe.Balance()

    elif n==4:
        c = int(input("Enter your years : "))
        d = int(input("Enter your Rate of Interest : "))
        e = int(input("Enter your Amount : "))
        pepe.Compound(c,d,e)
    else:
        f = int(input("Enter Your Account number "))
        g = str(input("Enter Your Name "))
