from math import *
def task1():
    x = float(input("Введите значение переменной x "))
    y = float(input("Введите значение переменной y "))
    z = float(input("Введите значение переменной z "))

    a = ((cos(x) * cos(y)) / (sin(x) * sin(y))) * (log(x) * log(y)) / (log(x) + log(y))
    b = log10(x + 1) - z ** (1 / 4) * x ** (1 / 2) + y ** (1 / 3)
    print("Значение переменной a =", round(a,4))
    print("Значение переменной b =", round(b,4))

def task2():
    x = float(input("Введите значение переменной x "))
    a = 2
    b = -1
    f = a*(((x**b) + x)/3) - (x**(b/4))
    print("Функция f(x) = ", round(f,4))

def task3():
    x = float(input("Введите значение переменной x "))
    f = cosh(sinh(1/(x**3)))**3
    print("Значение функции f(x) =  ", round(f,4))

def task4():
    V = float(input("Введите объем шара "))
    p = float(input("Введите во сколько раз увеличиться радиус "))
    r = (3*V)/(4*pi)**(1/3)
    r_new = r * p
    S_new = 4 * pi * (r_new**2)
    print("Площадь поверхности нового шара = ",round(S_new,4))

def task5():
    v = float(input("Введите скорость тела "))
    m = float(input("Введите массу планеты "))
    g = 9.8
    h = (0.5 * (v**2))/g
    print("Высота подъема тела = ",round(h,4))

def task6():
    Vpyr = float(input("Введите объем пирамиды "))
    P = float(input("Введите периметр основания "))
    h = float(input("Введите высоту пирамиды "))
    Scir = float(input("Введите радиус вписанной окружности "))
    k = float(input("Введите отношение высоты к радиусу основания "))
    r = P / (2*pi)#Радиус основания конуса
    Vpyr = (1/3)* Scir * h
    V_con = Vpyr
    print("Объем конуса = ", round(V_con,4))

def task7():
    a = float(input("Введите значение коэфициента A "))
    b = float(input("Введите значение коэфициента B "))
    c = float(input("Введите значение коэфициента C "))
    if (a >= -10) and (c <= 10):
        D = (b**2 - (4*a*c))**1/2
        if D < 0:
            print("Корней нет")
        if D > 0:
            x1 = (-b + D)/2*a
            x2 = (-b - D)/2*a
        if D == 0:
            print("Решений нет")
        print(min(x1,x2), max(x1,x2))

def task8():
    v1 = float(input("Введите скорость велосипедиста "))
    r = float(input("Введите диаметр колеса(в см) "))
    t = float(input("Введите время в минутах "))
    v1_ms = v1 * 1000/3600
    t_sec = t * 60
    s = v1_ms * t_sec #Расстояние
    c = r * pi #Длина окружности
    ob = s/c
    print(round(ob,4))

def task9():
    salary = float(input("Введите ежемесячную зарплату "))
    salaryDV = salary * 113/100
    print("Ежемесячная зарплата Геогрия до вычета составляет:", round(salaryDV,4))
task7()








