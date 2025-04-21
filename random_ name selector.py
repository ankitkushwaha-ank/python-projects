# import random
#
# # Specify the path to your file
# file_path = 'list.txt'
#
# # Read the file and pick a random name
# with open(file_path, 'r' ,) as file:
#     names = file.readlines()
#     random_name = random.choice(names).strip()  # Remove any trailing whitespace or newline
#     print(f"Randomly selected name: {random_name}")
#
# import random
#  # select a txt file for name of students
# file_path = "list.txt"
#
# with open(file_path , "r") as file:
#     names = file.readlines()
#     random_name  = random.sample([name.strip() for name in names] , 5)
#     print("---------------------------")
#     print("random group for 5 peoples")
#     print("---------------------------")
#
#     for name in random_name:
#         print(name)
#     print("---------------------------")

import random

file_name = "list.txt"

with open(file_name , "r") as file:

    names = file.readlines()
    random_names = random.sample([name.strip() for name in names] , 5)
    print("the group of 5 random persons are here:")

    for name in random_names:
        print(name)


# file_path = "list.txt"
#
# with open(file_path , "r") as file:
#     names = [name.strip() for name in file.readlines()]
#     if len(names) < 5:
#         print("error : not enough names in the file")
#     else:
#         random_names = random.sample(names , 5)
#         print("---------------------------")
#         print("random group for 5 peoples")
#         print("---------------------------")
#         for name in random_names:
#             print(name)
