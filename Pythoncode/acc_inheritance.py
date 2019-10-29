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

#account = Account("balance.txt")
#print("Current bal :",account.balance,"\n")
#print("bal after 200 withdrawer :",account.withdrawer(200),account.commit(),account.balance,"\n")
    
#print("bal after Depasit 500 :",account.deposit(500),account.commit(),account.balance,"\n")

class Checking(Account):
    """This class generate checkings account"""

    def __init__(self, filepath,fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount, fee):
        self.balance = self.balance - amount - fee

checking = Checking('balance.txt',1)
print(f'current bal: {checking.balance}')
print(f'bal after 45 deposit: {checking.deposit(1750)}',checking.commit(),checking.balance)
print('bal after 390 Transfer: ',checking.transfer(390,45),checking.commit(),checking.balance)
print(checking.__doc__)