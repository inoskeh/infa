from math import *
x = float(input("Введите значение переменной x "))
y = float(input("Введите значение переменной y "))
z = float(input("Введите значение переменной z "))

a = ((cos(x) * cos(y)) / (sin(x) * sin(y))) * (log(x) * log(y)) / (log(x) + log(y))
b = log10(x + 1) - z ** (1 / 4) * x ** (1 / 2) + y ** (1 / 3)
print("Значение переменной a =", a)
print("Значение переменной b =", b)

#task2
a = 2
b = -1
f = a*(((x**b) + x)/3) - (x**(b/4))
print("Функция f(x) = ", f)
