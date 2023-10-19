class Account:
    def __init__(self,name,amount) -> None:
        self.name = name
        self.amount = amount

    def deposit(self,fund):
        return self.amount  + fund
    
    def withdraw(self,fund):
        return self.amount - fund

    def query(self):
        query1 = input("Do you want to deposit or withdraw ? ")
        if query1 == "deposit" :
            print(f"Your account balance becomes {account1.deposit(fund_acc)}")

        elif query1 == "withdraw":
            print(f"Your account balance becomes {account1.withdraw(fund_acc)}")

while True:
    name_acc = input("Enter your name : ")

    amount_acc = int(input("Enter your account balance : "))

    fund_acc = int(input("Enter your fund : "))

    account1 = Account(name_acc,amount_acc)
    account1.query()
