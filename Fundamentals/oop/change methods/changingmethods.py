class User:
    def __init__(self, name, amount=0):  # Added default value for the 'amount' parameter
        self.name = name
        self.amount = amount

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount): 
        self.amount -= amount
        return self


    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

# Create User objects with different names.
omar = User("Omar")
Mohamed = User("Mohamed")
Sami = User("Sami")

# Perform transactions for the users.
# First user tarans
omar.make_deposit(500).make_deposit(1000).make_deposit(8000).make_withdrawal(2000).display_user_balance()
# second user trasactions
Mohamed.make_deposit(5000).make_deposit(7000).make_withdrawal(2000).make_withdrawal(3000).display_user_balance()
# Third user trasactions
Sami.make_deposit(50000).make_withdrawal(3000).make_withdrawal(3000).make_withdrawal(4000).display_user_balance()
# transfer money from omar to mohamed
omar.transfer_money(500,Mohamed)