while True:
    age = int(input("Enter your age: "))
    # nationality = input("country: ")

    if age >= 18 and age < 100:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")