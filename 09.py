def find_mean(number):
    total = sum(number)
    count = len(number)
    mean = total / count
    return mean


X = input("enter number separated by spaces")
Y = X.split()
Z = []
for y in Y:
    z = int(y)
    Z.append(z)

Z = [float(z) for z in X.split()]

mean = find_mean(Z)
print(mean)

import statistics
a = [11 ,12, 13,14]
mean = statistics.mean(a)
print(mean)

a = [10,20, 30, 40, 50]
F =[11,23,34,45,23]
Af = [a[i]*F[i] for i in range(len(a))]
mean = sum(Af)/sum(F)
print(mean)