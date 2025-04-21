num1 = int(input("enter the value1:"))
num2 = int(input("enter the value2:"))
opr = input("inter your opr:")

if opr == "+":
    print(num1+num2)
elif opr=="-":
    print(num1 - num2)
elif opr=="/":
    print(num1 / num2)
elif opr=="*":
    print(num1 * num2)
else:
    print("invalid opr")