print("""
+ add
-substact
* multiple
/ divide
""")
num1 = int(input("enter the value1:- "))
opr = input("inter your opr:- ")
num2 = int(input("enter the value2:- "))


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