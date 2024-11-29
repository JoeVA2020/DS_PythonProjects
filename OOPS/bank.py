class Bank:
    min_balance=2000
    balance=min_balance
    account='******3256'

class Actions(Bank):
    def credit(self,amount ):
        self.amount=amount
        Bank.balance+=amount
        print("Your ",Bank.account," has been credited",self.amount,'your bank balance is',Bank.balance)
    def debit(self,amount):
        self.amount=amount
        if(Bank.balance-amount<Bank.min_balance):
            print('Insufficient balance. Your balance is',Bank.balance)
        else:
            Bank.balance-=amount
            print("Your ", Bank.account, " has been debited",self.amount,'your bank balance is',Bank.balance)

class Person:
    def person_data(self,fname,lname,date):
        self.fname=fname
        self.lname=lname
        self.date=date

obj1=Actions()
obj1.debit(800)
obj1.credit(3200)
obj1.debit(3000)