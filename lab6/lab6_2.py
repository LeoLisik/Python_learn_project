from math import cos
try:
    m = int(input("Введите количество членов ряда = "))
except:
    print("Вы ввели не целое число! Будет установлено значение по умолчанию: 2")
    m = 2
try:
    x = float(input("Введите x = "))
except:
    print("Вы ввели не число! Будет установлено значение по умолчанию: 2")
    x = 2
S = 0
for n in range(1, m+1):
    Sn = cos(3 * n * x) / (1 + n ** 2)
    S += Sn
    print("n = ", n, "Sn = ", Sn, "S = ", S)
f = open('lab6_2.out', 'w')
try:
    f.write("n = ")
    f.write(str(n))
    f.write(" Sn = ")
    f.write(str(Sn))
    f.write(" S = ")
    f.write(str(S))
except:
    print("Запись в файл не удалась")
else:
    print("Файл успешно записан")
finally:
    f.close()
input("Press ENTER to close")
