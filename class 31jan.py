# print("x" * 7 , "Encapsulation in Python", "x" * 7)
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute
#
#     def deposit(self, amount):
#         self.__balance += amount
#         return f"New Balance: {self.__balance}"
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(1000)
# # print(account.__balance)  # ❌ Raises an AttributeError
# print(account.get_balance())  # ✅ Accessing through a method
#
# print("x" * 20)
#
# class public():
#     def __init__(self):
#         self.name =  "ankit"
#
#     def display_name(self):
#         print(self.name)
#
# obj1 = public()
# #accesbility
# obj1.display_name()
# print(obj1.name)
#
# print("x" * 20)
#
# class Private:
#     def __init__(self):
#         self.__salary = 40000  # Private variable self._variablename
#
#     def display_name(self):
#         print(self.__salary)  # Public method
#
# obj2 = Private()
# obj2.display_name()
#
# class Protected:
#     def __init__(self):
#         self._age = 22  # Protected attribute
#
# class subclass(Protected):
#     def display_age(self):
#         print(self._age)
#
# # Create an instance of the subclass
# obj = subclass()
#
# # Access the protected attribute using the instance of the subclass
# obj.display_age()  # Output: 22
# #
#
# print("x" * 7 , "Inheritance in python", "x" * 7)
#
# class Animal:  # Parent class
#     def speak(self):
#         return "Animal makes a sound"
#
# class Dog(Animal):  # Child class
#     def bark(self):
#         return "Dog barks"
#
# dog = Dog()
# print(dog.speak())  # Inherited from Animal
# print(dog.bark())   # Defined in Dog
#
# print("x" * 20)
#
# class Father:
#     def skill(self):
#         return "Good at Driving"
#
# class Mother:
#     def talent(self):
#         return "Good at Singing"
#
# class Child(Father, Mother):
#     pass
#
# c = Child()
# print(c.skill())
# print(c.talent())
#
# print("x" * 20)
#
#
# class Grandfather:
#     def house(self):
#         return "Owns a big house"
#
# class Father(Grandfather):
#     def car(self):
#         return "Owns a car"
#
# class Son(Father):
#     def bike(self):
#         return "Owns a bike"
#
# s = Son()
# print(s.house())  # Inherited from Grandfather
# print(s.car())    # Inherited from Father
# print(s.bike())   # Defined in Son
#
# print("x" * 20)
#
# # Python Inheritance
# # It allows to define a class that inherits all the methods and properties from another class.
#
# # Parent Class: the class being inherited from, also known as base class.
#
# # Child Class: the class that inherits from another class, also called derived class.
#
#
# # Create Parent class/Base Class
#
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# # Example usage:
# P1 = Person("Ankit" , "kushwaha")
# P1.printname()
#
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)  # Use super() to call parent's __init__
#         self.twelthpassingyear = year
#
#     def print_detail(self):
#         print(self.firstname, self.lastname, self.twelthpassingyear)
#
# S1 = Student("ankit" , "kushwaha" ,2022)
# S1.printname()
# S1.print_detail()
#
# -*- coding: utf-8 -*-
#1 feb 2025
# print("hello world")

# def fun():
#     print("hello world")
#
# fun()
#
# #syntax
#
#
# # def function_name(positional arguments):
#
# #ex:
#
# def square_add(a,b):
#     print("a = ",a)
#     print("b = ",b)
#     c = a*a + b*b
#     return c
#
# a = 2
# b = 3
#
# c= square_add(a,b)
# print(c)
#
# c = square_add(b,a)  # Note: order of arguments is swapped here
# print(c)
#
#
# def square_add(a,b):
#     global c  # Declare c as global to modify it inside the function
#     print("a =",a)
#     print("b =",b)
#     c = a*a + b*b  # Calculate the sum of squares and assign it to the global c
#
# a = 2
# b = 3
#
# square_add(a, b)  # Call the function, which will calculate c
#
# print(c)  # Print the value of the global c
#
#
# # global variable
# global x  # Declare x as global
# x = 10  # Initialize the global x
#
# def fun2(x):
#
#     x = x -5
#     print("Inside function:", x)  # Print x inside the function
#
# print("outside function", x)  # Print x outside the function (global x)
# fun2(x)  # Call fun2, passing the global x as an argument
#
# def square_add(a,b):
#     global c  # Declare c as global to modify it inside the function
#     print("a =",a)
#     print("b =",b)
#     c = a*a + b*b  # Calculate the sum of squares and assign it to the global c
#
# a = 2
# b = 3
#
# square_add(a, b)  # Call the function, which will calculate c
#
# print(c)  # Print the value of the global c
#
#
# def is_even(number):
#     return number % 2 == 0
#
# print(is_even(12))
# print(is_even(19))


# def even_or_not(num):
#     num = input("give me a number:-")
#     if num % 2 == 0:
#        print(f'{num} is even number')
#
#     else:
#        print(f'{num} is odd number')
#
# print(even_or_not)

#
# def even():
#     number = int(input("Enter the number:"))
#     if number % 2 == 0:
#         print("Even number")
#
#
# even()
#
# class ATM:
#     def __init__(self, pin, balance=0):  # constructor
#         self.pin = pin
#         self.balance = balance
#         self.logged_in = False
#
#     def authenticate(self, entered_pin):
#         if entered_pin == self.pin:
#             self.logged_in = True
#             print("Login successful.")
#         else:
#             print("Incorrect PIN. Please try again.")
#
#     def logout(self):
#         """Logout the user."""
#         self.logged_in = False
#         print("Logged out successfully.")
#
#     def check_balance(self):
#         if self.logged_in:
#             print(f"Your current balance is: ${self.balance}")
#         else:
#             print("Please log in first.")
#
#     def deposit(self, amount):
#         if self.logged_in:
#             if amount > 0:
#                 self.balance += amount
#                 print(f"Deposited ${amount}. Your new balance is ${self.balance}")
#             else:
#                 print("Amount should be greater than zero.")
#         else:
#             print("Please log in first.")
#
#     def withdraw(self, amount):
#         if self.logged_in:
#             if amount > 0 and amount <= self.balance:  # Corrected condition
#                 self.balance -= amount  # Subtract amount from balance
#                 print(f"Withdrew ${amount}. Your new balance is ${self.balance}")
#             else:
#                 print("Insufficient funds or invalid amount.")  # Improved message
#         else:
#             print("Please log in first.")
#
#     def password_change(self, old_pin, new_pin):
#         if self.pin == old_pin:
#             self.pin = new_pin
#             self.logged_in = False  # Log the user out after password change
#             print("Password changed successfully, Please login again")
#         else:
#             print("Old pin is incorrect")
#
#
# atm = ATM(pin=1234, balance=1000)
#
# # Authenticate user with a pin
# atm.authenticate(1234)
#
# # Check balance
# atm.check_balance()
#
# # Deposit money
# atm.deposit(500)
#
# # Withdraw money
# atm.withdraw(200)
#
# # Logout
# atm.logout()
#

#
# sbi = ATM(pin=9876, balance=1)
#
# sbi.authenticate(9876)
# sbi.check_balance()
#
# sbi.deposit(20000)
#
# sbi.withdraw(5000)
#
# sbi.password_change(9876, 3456)

# class car:
#     def __init__(self , brand ,model, fuel_capacity , fuel = 0):
#         self.car_brand = brand
#         self.car_model = model
#         self.car_fuel_capacity = fuel_capacity
#         self.car_current_fuel = fuel
#
#     def refueling(self, ammount):
#         if ammount<= 0:
#             return "you cannot pay in minus (Invalid fuel amount)"
#         if self.car_current_fuel + ammount > self.car_fuel_capacity
#             self.car_current_fuel = self.car_fuel_capacity
#             return "your tank is full"
#         self.car_current_fuel += ammount
#         return f'your car is refueled {ammount} litres, your current fuel level is {self.car_current_fuel}'
#
# car_details = car("fortuner", "legender", 70, 10)
#
# print(car_details.refuel(20))

#sir code
class car:
    def __init__(self, make, model, year, fuel_level=100):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"The {self.make} {self.model}'s engine is now running.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print(f"The {self.make} {self.model}'s engine has been turned off.")
        else:
            print(f"The {self.make} {self.model}'s engine is already off.")

    def drive(self, distance):
        if self.engine_on:
            fuel_used = distance * 0.1  # Assuming 0.1 fuel consumption per mile
            if self.fuel_level >= fuel_used:
                print(f"Driving {distance} miles. Fuel used: {fuel_used}%.")
                self.fuel_level -= fuel_used
            else:
                print(f"Remaining fuel: {self.fuel_level}%.")
                print("Not enough fuel to drive this distance.")
        else:
            print("Start the engine before driving.")

    def refuel(self, amount):
        if amount + self.fuel_level <= 100:
            self.fuel_level += amount
            print(f"Refueled {amount}%. New fuel level: {self.fuel_level}%.")
        else:
            self.fuel_level = 100
            print("The tank is full! Fuel level is now 100%.")

    def get_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")  # Corrected f-string
        print(f"Fuel Level: {self.fuel_level}%")
        print(f"Engine is {'on' if self.engine_on else 'off'}.")

    # Example usage:
    my_car = car("TATA", "NEXON", 2021)  # Corrected year 2821 to 2021

    my_car.get_info()
    my_car.start_engine()
    my_car.drive(50)
    my_car.refuel(30)
    my_car.get_info()
