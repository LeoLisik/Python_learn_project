x = float(input("Введите x = "))
y = float(input("Введите y = "))
if x > -1 and y < 4:
    b = x ** 2 + 5 * y
elif x < -1 or 4 <= y < 10:
    b = abs(3 * x ** 2 - 5 * y)
else:
    b = y
print("b = ", b)
input("Press button to close")
