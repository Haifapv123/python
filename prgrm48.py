class Bank:
    def __init__(self):
        self.name=input("Enter name: ")
        self.b=int(input("Enter balance: "))

    def deposit(self):
        self.b+=int(input("Deposit: "))

    def withdraw(self):
        a=int(input("Withdraw: "))
        if a<=self.b:
            self.b-=a
        else:
            print("Insufficient balance")

    def display(self):
        print(self.name,self.b)

x=Bank()
x.deposit()
x.withdraw()
x.display()
