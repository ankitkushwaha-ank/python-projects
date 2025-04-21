import matplotlib.pyplot as plt

x = (10.2, 12.3, 11.2, 14)
y = (1, 2, 3, 4)

plt.figure()
plt.bar(x, y)
plt.plot(x, y, marker='o', label='Prime Numbers')

plt.xlabel("a-axis")
plt.ylabel("b-axis")
plt.title("name")

plt.legend()
plt.show()
