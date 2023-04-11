class BankAccount:
    def __init__(self,account_number,balence,date_opening,name) :
        self.account_number=account_number
        self.balence=balence
        self.date_opening=date_opening
        self.name=name
    def Deposit(self,amount):
        self.balence+=amount
    def Withdraw(self,amount):
        if amount>balence:
            print("Cancel")
        else :
            balence=balence-amount
    def check_balence(self):
        print()