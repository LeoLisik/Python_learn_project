from math import sqrt
try:
    x = float(input("Введите x = "))
    y = float(input("Введите y = "))
except:
    print("Некорректный ввод! Значения переменных приняты за единицу.")
    x = 1
    y = 1
hyp = sqrt(x ** 2 + y ** 2)
if x >= 0 and y > 0:
    r = 3
elif x >= 0 and y <= 0:
    r = 4
else:
    r = 0
if hyp <= r:
    print("True")
else:
    print("False")
