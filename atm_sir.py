
class ATM:
    def __init__(self, pin, balance=0):  # constructor
        self.pin = pin
        self.balance = balance
        self.logged_in = False

    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.logged_in = True
            print("Login successful.")
        else:
            print("Incorrect PIN. Please try again.")

    def logout(self):
        """Logout the user."""
        self.logged_in = False
        print("Logged out successfully.")

    def check_balance(self):
        if self.logged_in:
            print(f"Your current balance is: ${self.balance}")
        else:
            print("Please log in first.")

    def deposit(self, amount):
        if self.logged_in:
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. Your new balance is ${self.balance}")
            else:
                print("Amount should be greater than zero.")
        else:
            print("Please log in first.")

    def withdraw(self, amount):
        if self.logged_in:
            if amount > 0 and amount <= self.balance:  # Corrected condition
                self.balance -= amount  # Subtract amount from balance
                print(f"Withdrew ${amount}. Your new balance is ${self.balance}")
            else:
                print("Insufficient funds or invalid amount.")  # Improved message
        else:
            print("Please log in first.")

    def password_change(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            self.logged_in = False  # Log the user out after password change
            print("Password changed successfully, Please login again")
        else:
            print("Old pin is incorrect")


atm = ATM(pin=1234, balance=1000)

# Authenticate user with a pin
atm.authenticate(1234)

# Check balance
atm.check_balance()
atm.logout()
atm.check_balance()
atm.authenticate(1234)
atm.deposit(1453)
atm.check_balance()

#
# # Deposit money
# atm.deposit(500)
#
# # Withdraw money
# atm.withdraw(200)
#
# # Logout
# atm.logout()

