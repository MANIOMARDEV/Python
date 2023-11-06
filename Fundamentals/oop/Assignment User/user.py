class User:
    def __init__(self, name, amount=0):  # Added default value for the 'amount' parameter
        self.name = name
        self.amount = amount

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount): 
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

# Create User objects with different names.
omar = User("Omar")
Mohamed = User("Mohamed")
Sami = User("Sami")

# Perform transactions for the users.
# First user tarans
omar.make_deposit(500)
omar.make_deposit(1000)
omar.make_deposit(8000)
omar.make_withdrawal(7000) 
omar.display_user_balance()
# second user trasactions
Mohamed.make_deposit(5000)
Mohamed.make_deposit(7000)
Mohamed.make_withdrawal(2000)
Mohamed.make_withdrawal(3000)
Mohamed.display_user_balance()
# Third user trasactions
Sami.make_deposit(50000)
Sami.make_withdrawal(3000)
Sami.make_withdrawal(3000)
Sami.make_withdrawal(4000)
Sami.display_user_balance()

# transfer money from omar to mohamed
omar.transfer_money(500,Mohamed)