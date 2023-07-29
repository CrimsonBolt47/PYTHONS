class Account:  #class

    def __init__(self,filepath): #constructor
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance= int(file.read())  #instance variable

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount

    

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):     #inheritence
    """ hello!"""          #doc string(similiar to comment specific to class)

    type="checking" #class variable
    
    def __init__(self,filepath, fee):
        Account.__init__(self, filepath) 
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee


checking=Checking("balance.txt", 1) #object declaration
#account=Account("balance.txt")  
#print(account.balance) 
#account.withdraw(100)
#print(account.balance)
#account.commit() 
print(checking.__doc__)
checking.transfer(110)
print(checking.balance)
checking.commit()

