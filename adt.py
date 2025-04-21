# import json
# class COLLEGE:
#     def __init__(self,name,roll_no,batch):
#         self.student = name
#         self.Roll = roll_no
#         self.Batch = batch
#         logged_in = False
#
#     def register(self):
#         user_name = input('input username: ')
#         password =input('enter your pass: ')
#
#         data = {user_name :password }
#     # Open the file in append mode and write the input with a newline
#         with open("data.json", "a") as file:
#             json.dump(data,file , indent=4)
#
#         print("you are registered successfully!")

import json

# Load users from the JSON file
with open("data.json", "r") as file:
    users = json.load(file)  # Convert JSON to dictionary

# Take login credentials from user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if username exists and password matches
if username in users and users[username] == password:
    print("✅ Login Successful!")
else:
    print("❌ Invalid Credentials! Please try again.")


# clg = COLLEGE('Ankit',854,2)
# clg.loggin()



