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

def decimal_in_new_numeral_system(number,base):
    result = ''
    intp = int(number)
    frp = number - intp
    while intp > 0:
        r = intp % base
        result = str(r) + result
        intp = intp // base
    result += '.'
    pr = 4
    while frp > 0 and pr > 0:
        frp *= base
        digit = int(frp)
        result += str(digit)
        frp -= digit
        pr -= 1
    return result
def task3():
    number = float(input("Введите десятичное число: "))
    base = int(input("Введите систему счисления: "))
    result = decimal_in_new_numeral_system(number,base)
    print(f"Результат: {result}")


def task5():
    a = float(input("Введите значение а: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    if (b < a < c) or (c < a < b):
        num = a
    elif (a < b < c) or (c < b < a):
        num = b
    else:
        num = c
    dnum = num * 2
    print(num, dnum)

def task6():
    def backterium(amount, minutes):
        number_of_bacteria = amount
        for i in range(1, minutes):
            number_of_bacteria = number_of_bacteria * 2
        return number_of_bacteria

    start_amount = int(input("Введите начальное количество бактерий"))
    minutes = int(input("Введите время: "))

    print(f"новое количество бактерий спустя заданное время = {backterium(start_amount, minutes)}")

def task8():
    n = int(input("Введите n: "))
    x = float(input("Введите x: "))

    S = x
    one = 3
    two = 5
    for i in range(1, n):
        S += ((-1) ** i) * (x ** one) / two
        one += 2
        two += 3

    print(f"S = {S}")
    
def task9():
    sum = 0  # создали переменную для суммы
    i = 1  # создали переменную-итератор
    while i < 9:
        j = 1
        sum1 = 0
    while j < i + 1:
        sum1 += (i - j) ** (1 / 3)
        j += 1
        sum += sum1
        i += 1

    print("sum = ",round(sum,4))
    mul = 1
    i = 1
    while i < 6:
        j = 1
        mul1 = 1
        while j < i + 1:
            mul1 *= j ** i
            j+=1
        i+=1
        mul *= mul1

    print(f"mul = {mul}")

    mul = 1
    i = 1
    while i < 9:
        sum = 0
        j = i
        while (j < 2 * i):
            sum1 = 0
            k = i + j
            while (k < 2 * (i + j) + 1):
                sum1 += (3 * i - 2 * (k + 0.2 * j))
                k += 1
            sum += sum1
            j += 1
        mul *= sum
        i += 1
    print(f"mul = {mul}")

def task10():
    def factorial(i):
        fact = i
        for i in range(1, i):
            fact = fact * i

        return fact

    x = float(input("Введите x: "))
    eps = float(input("Введите погрешность: "))

    i = 1
    sum = 0
    # print(sum)
    print("Аналитическое значение: ", round(sin(x) ** 2, 4))

    while (abs(sin(x) ** 2 - sum) > eps):
        sum += ((-1) ** (i + 1)) * ((2 ** (2 * i - 1)) / factorial(2 * i)) * (x ** (2 * i))
        i += 1

    print("Вычесленное значение: ", round(sum,4))

task3()
