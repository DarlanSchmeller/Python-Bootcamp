### Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
# - owner
# - balance
# and two methods:
# - deposit
# - withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner.capitalize()
        self.balance = balance

    def deposit(self, deposit_value):
        self.balance = self.balance + deposit_value
        print(f'Deposit of ${deposit_value} has been approved! \nCurrent Balance in {self.owner} account: ${self.balance}')

    def withdraw(self, withdraw_value):
        if withdraw_value <= self.balance:
            self.balance = self.balance - withdraw_value
            print(f'Withdraw of ${withdraw_value} approved. \nCurrent Balance in {self.owner} account: ${self.balance}')
        else:
            print(f'Withdraw of ${withdraw_value} denied. \nReason: Insufficient Funds in {self.owner} account!')

    def __str__(self):
        return f'Account Owner: {self.owner}'

    def __len__(self):
        return self.balance

my_bank_account = BankAccount('darlan', 500)
print(my_bank_account)
print(len(my_bank_account))
my_bank_account.deposit(378)