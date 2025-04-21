print("""
a = add(+)
s = sustract(-)
m = multple(*)
d = divide(/)
""")
num1 = int(eval(float(input("enter the value1:-"))))
num2 = int(eval(float(input("enter the value2:-"))))
opr = input("inter your opr:-")

if opr == "a":
    print(num1+num2)
elif opr=="s":
    print(num1 - num2)
elif opr=="d":
    print(num1 / num2)
elif opr=="m":
    print(num1 * num2)
else:
    print("invalid opr")