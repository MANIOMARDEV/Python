class BankAccount:
    accounts = []  # Class variable to store all accounts

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate  # Instance variable for interest rate
        self.balance = balance  # Instance variable for account balance
        BankAccount.accounts.append(self)  # Append the current instance to the accounts list

    def deposit(self, amount):
        self.balance += amount  # Increase the account balance by the given amount
        return self  # Return the instance to allow method chaining

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount  # Decrease the account balance by the given amount if sufficient funds are available
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5  # Charge a $5 fee for insufficient funds
        return self  # Return the instance to allow method chaining

    def display_account_info(self):
        print(f"Balance: {self.balance}")  # Display the account balance
        return self  # Return the instance to allow method chaining

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)  # Calculate and add interest to the account balance
        return self  # Return the instance to allow method chaining

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()  # Display information for all accounts

# Create two bank account instances
Account1 = BankAccount(0.08, 4000)
Account2 = BankAccount(0.07, 8000)

# Perform operations on Account1 and Account2
Account1.deposit(500).deposit(30).deposit(50).withdraw(200).yield_interest().display_account_info()
Account2.deposit(300).deposit(500).withdraw(100).withdraw(20).withdraw(10).withdraw(10).yield_interest().display_account_info()

# Display information for all accounts
BankAccount.print_all_accounts()