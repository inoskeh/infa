from math import *
x = float(input("Введите значение переменной x "))
y = float(input("Введите значение переменной y "))
z = float(input("Введите значение переменной z "))

    a = ((cos(x) * cos(y)) / (sin(x) * sin(y))) * (log(x) * log(y)) / (log(x) + log(y))
    b = log10(x + 1) - z ** (1 / 4) * x ** (1 / 2) + y ** (1 / 3)

    print("{0:.4f} text {1:.4f}".format(a, b))
    print("Значение переменной b =", b)
