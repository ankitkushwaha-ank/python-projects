#question 1
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")

# question 2
class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())


Str_man = StringManipulator()
Str_man.getString()    #input ankit kushwaha
Str_man.printString()   #output ANKIT KUSHWAHA


question 3
Accept comma-separated numbers from the user
numbers = input("Enter comma-separated numbers: ")

# Generate list and tuple
num_list = numbers.split(",")
num_tuple = tuple(num_list)

# Print the results
print("List:", num_list)  #output = List: ['22', '24', '26', '27']
print("Tuple:", num_tuple)  #output = Tuple: ('22', '24', '26', '27')

#question 4
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


#question 5
from collections import Counter


def word_frequency():
    text = input("Enter a sentence: ")
    words = text.split()
    freq = Counter(words)

    for word in sorted(freq.keys()):
        print(f"{word}:{freq[word]}")


# Run the function
if __name__ == "__main__":
    word_frequency()
