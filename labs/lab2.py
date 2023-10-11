from math import *
def sqrt(n):
    if n >= 0 and int(n**(1/2))** 2 == n:
        return True
    else:
        return False
def cub(n):
    if int(n**(1/3)) ** 3 == n:
        return True
    else:
        return False
def task1():
    while True:
        n = float(input("Введите число "))
        if sqrt(n):
            print(f"{n} квадрат целого числа")
        else:
            print(f"{n} не квадрат целого числа")
        if cub(n):
            print(f"{n}куб целого числа")
        else:
            print(f"{n} не куб целого числа")
task1()
