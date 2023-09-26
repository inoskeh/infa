from math import *
x = float(input("Введите значение переменной x "))
y = float(input("Введите значение переменной y "))
z = float(input("Введите значение переменной z "))
a = ((cos(x)*cos(y))/(sin(x)*sin(y)))*(log(x)*log(y))/(log(x)+log(y))
b = log10(1 + x) - z**(1/4)*sqrt(x) + y**(1/3)
print("Значение перменной a =",a)
print("Значение переменной b =",b)

