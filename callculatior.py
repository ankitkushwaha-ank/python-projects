v1 = int(input("enter the first value: "))
opr = input("enter what you want to do :")
v2 = int(input("enter your second value :"))

if opr == "+":
    print(v1 + v2)
elif opr == "-":
    print(v1 - v2)
elif opr == "*":
    print(v1 * v2)
elif opr == "/":
    print(v1 / v2)

else:
    print('your opr is wrong:')