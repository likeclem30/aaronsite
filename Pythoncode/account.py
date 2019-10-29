class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())
    
    def withdrawer(self, amount):
        self.balance = self.balance -amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open (self.filepath,'w') as file:
            file.write(str(self.balance))

account = Account("balance.txt")
print("Current bal :",account.balance,"\n")
print("bal after 200 withdrawer :",account.withdrawer(200),account.commit(),account.balance,"\n")
    
print("bal after Depasit 500 :",account.deposit(500),account.commit(),account.balance,"\n")