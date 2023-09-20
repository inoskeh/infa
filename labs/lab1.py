from math import *
def task1():
  x = float(input("Введите значение переменной x"))
  y = float(input("Введите значение переменной y"))
  z = float(input("Введите значение переменной z"))
  a = ((cos(x)*cos(y))/ (sin(x)*sin(y))) * ((log1p(x) * log1p(y))/(log1p(x) + log1p(y)))
  b = log10(1 + x) - z**(1/4)*sqrt(x) + y**(1/3)
  print("Значение перменной a =",a)
  print("Значнние переменной b =",b)
