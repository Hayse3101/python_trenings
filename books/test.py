from random import *

arr9 = [randint(0, 9) for _ in range(10)]
print(f"Список: {arr9}")

for i in arr9:
    if arr9.index(i) % 2 == 0:
        pass

for i in range(len(arr9)):
    for j in range(len(arr9)):
        if arr9[i] < arr9[j]:
            arr9[i], arr9[j] = arr9[j], arr9[i]
