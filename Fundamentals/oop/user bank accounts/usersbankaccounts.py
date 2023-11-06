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
        return f"Balance: {self.balance}"  # Return the account balance as a string

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)  # Calculate and add interest to the account balance
        return self  # Return the instance to allow method chaining

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print(account.display_account_info())  # Display information for all accounts

# Define a User class to represent a user with two bank accounts.

class User:
    # Constructor to initialize a User object with a name.
    def __init__(self, name):
        self.name = name
        # Create two bank accounts, "Account1" and "Account2," and store them in a dictionary.
        self.account = {
            "Account1": BankAccount(0.08, 4000),  # Initialize Account1 with an interest rate of 0.08 and an initial balance of 4000.
            "Account2": BankAccount(0.09, 7000)   # Initialize Account2 with an interest rate of 0.09 and an initial balance of 7000.
        }

    # Method to display the user's account balances.
    def display_user_balance(self):
        # Print the user's name and the balance information of both accounts.
        print(f"User: {self.name}, Account1 {self.account['Account1'].display_account_info()}")
        print(f"User: {self.name}, Account2 {self.account['Account2'].display_account_info()}")
        return self  # Return self to allow method chaining.

    # Method to transfer money from the user's Account1 to another user's Account1.
    def transfer_money(self, amount, user):
        # Deduct the specified amount from the user's Account1.
        self.account['Account1'].balance -= amount
        # Add the same amount to the recipient user's Account1.
        user.account['Account1'].balance += amount
        # Display updated balances for both the sender and recipient.
        self.display_user_balance()
        user.display_user_balance()
        return self  # Return self to allow method chaining.

# Create a User instance named "Omar."
Omar = User("Omar")

# Deposit 200 units of currency into "Account1" belonging to user "Omar."
Omar.account['Account1'].deposit(200)

# Display the updated balances for both "Account1" and "Account2" of user "Omar."
Omar.display_user_balance()