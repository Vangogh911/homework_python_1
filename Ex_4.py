# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

sector = int(input("Введите номер четверти: "))
if sector == 1:
    print("x = (1 -> n), y = (1 -> n)")
elif sector == 2:
    print("x = (-1 -> -n), y = (1 -> n)")
elif sector == 3:
    print("x = (-1 -> -n), y = (-1 -> -n)")
elif sector == 4:
    print("x = (1 -> n), y = (-1 -> -n)")
else:
    print("Нет четверти с таким номером")
