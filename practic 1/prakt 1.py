from math import cos, sin, exp
try:
    x = float(input("Введите x = "))
    y = float(input("Введите y = "))
    z = float(input("Введите z = "))
    a = float(input("Введите a = "))
    c = float(input("Введите c = "))
    b = float(input("Введите b = "))
    d = float(input("Введите d = "))
    f = float(input("Введите f = "))
except:
    print("Обнаружена ошибка ввода, значения всех переменных приняты за единицу")
    x = 1
    y = 1
    z = 1
    a = 1
    c = 1
    b = 1
    d = 1
    f = 1
result = (exp(x)) - ((y**2 + 12*x*y - 3*x**2) / (18*y-1))
print("Результат первой формулы = ", result)
try:
    result = ((cos(x) ** x) / sin(x)) - (x * y * z) + ((a*x**2 + b*x + c) / (d*x**3 - f))
    print("Результат второй формулы = ", result)
except:
    print("Обнаружено деление на ноль во второй формуле. Вселенная схлопывается...")
