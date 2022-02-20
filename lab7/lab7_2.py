from math import atan
from math import sqrt
try:
    k1 = float(input("Введите k1 = "))
except:
    print("Вы ввели не целое число! Будет установлено значение по умолчанию: 25")
    k1 = 25
try:
    k2 = float(input("Введите k2 = "))
except:
    print("Вы ввели не число! Будет установлено значение по умолчанию: 5")
    k2 = 5
z = -1
while True:
    if z == 0:
        z += 0.5
        continue
    y = (sqrt(k1+z) - k2) / (k2 * atan(0.1 * z))
    print("z = ", z, "y(z) = ", y)
    z += 0.5
    if z > 6:
        break
file = open('lab7_2.out', 'w')
try:
    file.write("z = ")
    file.write(str(z - 0.5))
    file.write(" y(z) = ")
    file.write(str(y))
except:
    print("Запись в файл не удалась")
else:
    print("Файл успешно записан")
finally:
    file.close()
input("Press ENTER to close")
