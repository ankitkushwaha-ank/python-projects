#Banking system for a ATM
print("*"*12, "central bank of india" , "*"*12)
# customer insert there atm card to atm
print('--your card has been inserted successfully--')
class ATM:
    def __init__(self,account_holder,pin,balance=1000):
        self.name = account_holder
        self.atm_pin = pin
        self.bank_balance = balance
        self.logged_in = False



    def authenticate(self,entered_pin):
        entered_pin = int(input('Enter your atm pin:-'))
        if entered_pin == self.atm_pin:
            self.logged_in = True
            print("your are logged in successfully")

        else:
            print('*invalid atm pin please try again*')



    def logout(self):
        self.logged_in = False
        print("you are logged out successfully")

    def check_balance(self):
        if self.logged_in:
            print(f"bank balance - ${self.bank_balance} ")
        else:
            print("please loggin first :)")

    def deposit(self , amount):
        amount = int(input('Deposit money:-'))
        if self.logged_in:
            if amount > 0:
                self.bank_balance += amount
                print(f"your account has credited {amount} rupees.")
                print(f"your current bank balance is {self.bank_balance}")

            else:
                print("use sufficient balance")
        else:
            print("login first")

    def withdraw(self,amount):
        amount = int(input('withdrawn amount:-'))
        if self.logged_in:
            if amount > self.bank_balance:
                print("No sufficient balance")
            else:
                self.bank_balance -= amount
                print(f"your account has debited {amount} rupees successfully")
                print(f" your current bank balance is {self.bank_balance}")
        else:
            print("please login first")

bank = ATM("Ankit kushwaha",1234,4555)

print('''
which service do you want:)
   1 - login to your account 
   2 - check your balance
   3 - deposit money 
   4 - withdraw money  
   99 - logout 
     ''')
user_input =""
while user_input != "q":
    user_input = input("choose any option or q for quit :-")
    if user_input.isdigit():
        if int(user_input) == 1:
            bank.authenticate(1234)
        if bank.logged_in:
            if int(user_input) == 1:
                continue
            if int(user_input) == 2:
                print(f'your bank balance is: ${bank.bank_balance}')

            elif int(user_input) == 3:
                bank.deposit(0)

            elif int(user_input) == 4:
                bank.withdraw(0)

            elif int(user_input) == 99:
                bank.logout()
            else:
                print("invalid input")
        else:
            print('PLEASE LOGIN FIRST')
    else:
        print('invalid option')





















