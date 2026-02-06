class Amount:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self, amount):
            self.balance -= amount
            print(f"Rs {amount} was debited from account: {self.account_no}")
            print("Total balance =", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} was credited to account: {self.account_no}")
        print("Total balance =", self.get_balance())
        
    def get_balance(self):
        return self.balance
s1 = Amount(10000, 56565) 
s1.debit(500)
s1.credit(50000)
