import math
def task1():
  x = float(input(""))
  y = float(input(""))
  z = float(input(""))
  a = ((math.cos(x)*math.cos(y))/ (math.sin(x)*math.sin(y))) * ((math.log1p(x) * math.log1p(y))/(math.log1p(x) + math.log1p(y)))
  b = math.log10(1 + x) - z**(1/4)*math.sqrt(x) + y**(1/3)
  print("Значение перменной a =",a)
  print("Значнние переменной b =",b)
