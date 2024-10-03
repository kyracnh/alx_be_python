class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0.0
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount:.2f} into the account.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.2f} from the account.")
        elif amount < self.account_balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
