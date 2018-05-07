# In this assignment you are going to test your knowledge of class composition. Your task is to create a class which represent a "Bank Account". The Bank Account will have the following properties.
# Bank Account:
# - First Name
# - Last Name
# - Middle Name
# - Account Type
# - Balance
# - Status (Opened/Closed/Freeze)
# Here are the features that needs to be implement:
# - A user should be able to open a bank account provided they have the initial balance of $10
# - User should be able to transfer money from one bank account to another
# - A user should be able to withdraw money from the bank account
# - The app should charge $-35 fees if the bank account is below $0

class User:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.bank_accounts = []

    def addBankAccount(self,bank_account):
        self.bank_accounts.append(bank_account)

    def __repr__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class BankAccount:
    def __init__(self, user, account_type, balance,status):
        self.user = user
        self.account_type = account_type
        self.status = status
        self.balance = 0

    def open_account(self, account, deposit):
        if deposit >= 100:
            print(f"A {self.account_type} account was created.")
            self.balance += deposit
            print(self.balance)
        else:
            print("Please deposit $100 to open account.")

    def transfer(self, amount, toAccount):
        toAccount.balance += amount
        self.balance -= amount
        print(f"A total of {amount} was transferred from {self.account_type} to {toAccount.account_type}.")
        print(f"The new balance for {self.account_type} account is {self.balance}.")
        print(f"The new balance for {toAccount.account_type} acount is {toAccount.balance}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"New balance after the {amount} withdrawal is {self.balance}.")


    def charge_fee(self):
        if self.balance < 0:
            self.balance -= 35
            print(self.balance)

    def __repr__(self):
        return f"{self.user} {self.account_type} {self.balance}"


user = User("Pedro", "H", "Martinez")
checking_account = BankAccount(user, "checking", 0, "Open")
savings_account = BankAccount(user, "savings", 0, "Open")

checking_account.open_account(checking_account, 100)
savings_account.open_account(savings_account, 100)

user.addBankAccount(checking_account)
user.addBankAccount(savings_account)

checking_account.transfer(10, savings_account)

checking_account.withdraw(110)

checking_account.charge_fee()
