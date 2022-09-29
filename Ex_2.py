# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

arr = []

for x in range(2):
    for y in range(2):
        for z in range(2):
            # print(x, y, z)
            # print(not (x or y or z))
            # print(not x and not y and not z)
            # print("")
            arr.append(not (x or y or z)==(not x and not y and not z))

if False in arr:
    print("Утверждение ложно")
else:
    print("Утверждение истинно")
