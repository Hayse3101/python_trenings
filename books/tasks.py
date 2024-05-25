# -------------------- Задачи предоставленные в книгах --------------------

# ------------ Задача №1 ------------
day = int(input("Какой сегодня день? "))
month = input("Какой месяц? ")

print(f"Дата {day} - {month} 2024 года")

# ------------ Задача №2 ------------
this_year = int(input("Какой сейчас год? "))
year_of_birth = int(input("Ваш год рождения? "))

print(f"Ваш возраст {this_year - year_of_birth}")

# ------------ Задача №3 ------------
distance = int(input("Введите расстояние в милях: "))
print(f"Растояние в киллометрах - {distance * 1.6}")

# ------------ Задача №4 ------------
nums1 = int(input("Введите количество чисел в списке: "))
arr1 = [2 ** i for i in range(nums1)]
print(f"Ваш список: {arr1}")

# ------------ Задача №5 ------------
nums2 = int(input("Введите длину списка: "))
arr2 = [5 * i + 3 for i in range(nums2)]
print(f"Ваш список - {arr2}")

# ------------ Задача №6 ------------
nums3 = int(input("Введите число: "))
if nums3 % 3 == 0:
    print("Число делится на 3")
else:
    print("Число не делится на 3")

# ------------ Задача №7 ------------
nums4 = int(input("Факториал какого числа: "))
factorial = 1

if nums4 > 0:
    while nums4 > 1:
        factorial *= nums4
        nums4 -= 1

    print(f"Факториал - {factorial}")
else:
    print("Ваше число меньше нуля")

# ------------ Задача №8 ------------
nums5 = int(input("Сколько чисел фибоначчи: "))
fib1 = 1
fib2 = 1
fib_sum = 0
i = 1
while i < nums5:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(f"Числа фибоначчи: {fib_sum}")
    i += 1

# ------------ Задача №9 ------------


def func1(arr: list) -> int:
    i = 0
    max_value = 0
    min_value = 0
    while i < len(arr):
        print(f" - Итерация {i} - arr[i] = {arr[i]}")
        if max_value < arr[i]:
            min_value = max_value
            max_value = arr[i]
        else:
            min_value = arr[i]
        print(f" -- Итерация {i} - min_value = {min_value}, max_value = {max_value}")
        i += 1
    return min_value


arr3: list = [3, 1, 5, 6, 2, 9, 0, 7, 8]
print(f"Второе по величине число в списке - {func1(arr3)}")

# ------------ Задача №10 ------------


def func2(num: int) -> int:
    i: int = 0
    sum_nums: int = 0
    while i < num:
        if i % 2 != 0:
            sum_nums += i
        i += 1

    return sum_nums


nums7: int = int(input("Введите количество чисил: "))
print(f"Сумма нечетных чисел = {func2(nums7)}")

# ------------ Задача №11 ------------
num1 = int(input("Введите число: "))
arr4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

digit1 = 0
while num1 > 0:
    digit1 = num1 % 10
    for i in range(11):
        if digit1 == i:
            arr4[i] += 1
    num1 = num1 // 10

print(f"В ведённом числе 0 - {arr4[0]}, 1 - {arr4[1]}, 2 - {arr4[2]}, 3 - {arr4[3]}, 4 - {arr4[4]},"
      f" 5 - {arr4[5]}, 6 - {arr4[6]}, 7 - {arr4[7]}, 8 - {arr4[8]}, 9 - {arr4[9]}")

# ------------ Задача №12 ------------
num2 = int(input("Введите число: "))
digit2 = 0
digit_str2 = ""

while num2 > 0:
    digit2 = num2 % 10
    digit_str2 += str(9 - digit2)
    num2 = num2 // 10

print(f"Изменённое число - {digit_str2}")

# ------------ Задача №13 ------------
arr5 = [4, 12, 5, 0, 64, 10, 5]
digit_str1 = ""
for i in arr5:
    digit_str1 += str(i)

print(f"Объединенные числа из списка - {digit_str1}")

# ------------ Задача №14 ------------
arr6 = [3, 1, 5, 0, 2, 4]
arr7 = [3, 2, 5, 0, 2, 4]
count1 = 0
flag1 = True

equality = "У списков разная длина" if len(arr6) != len(arr7) else "Списки одинаковой длины"
for i in arr6:
    for j in arr7:
        if i == j:
            count1 += 1
            break
    else:
        print("Списки не равны")
        flag1 = False
    if flag1:
        pass
    else:
        break
    count1 = 0
else:
    print("Списки равны")
print(equality)

# ------------ Задача №15 ------------
arr8 = [2, 5, 6]
num8 = int(input("Введите верхнюю границу: "))
digit_sum1 = 0

for i in range(0, num8 + 1):
    if i in arr8:
        continue
    else:
        digit_sum1 += i

print(f"Сумма чисел согласно условиям - {digit_sum1}")

# ---------------------- Задание №16 ----------------------
num1 = int(input("Введите число a: "))
num2 = int(input("Введите число b: "))
num3 = int(input("Введите число c: "))

if (num1 + num2 > num3) and (num2 + num3 > num1) and (num3 + num1 > num2):
    print(f"Треугольник может существовать!")
else:
    print(f"Треугольник не может сущетвовать!")

# ---------------------- Задание №17 ----------------------
num4 = int(input("Введите число a: "))
num5 = int(input("Введите число b: "))
num6 = int(input("Введите число c: "))

digit = 0
if num4 - num5 == num5 - num6:
    print("Числа пренадлижат к арифметической прогресии")
else:
    print("Числа не пренадлижат к арифмитическйо прогресии")

# ---------------------- Задание №18 ----------------------
arr1 = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
num7 = int(input("Введите день недели: "))

for i in range(len(arr1)):
    if num7 == i + 1:
        print(f"Сегодня - {arr1[num7 - 1]}")
        break
else:
    print("Вы ввели некорректные значения!")

# ---------------------- Задание №19 ----------------------
try:
    num8 = int(input("Введите первое число: "))
    num9 = int(input("Введите второе число: "))

    res = "Первое число больше" if num8 > num9 else "Второе число больше"
    print(res)

except ValueError:
    print("Некорректные значения")

# ---------------------- Задание №20 ----------------------
num_a1 = int(input("Введите значение A: "))
num_b1 = int(input("Введите значение B: "))

if num_a1 != 0:
    print("Решение x = (B - 1) / A - 1")
elif num_a1 == 0 and num_b1 != 0:
    print("Решений у уравнения нет")
elif num_a1 == 0 and num_b1 == 1:
    print("Решение любое число!")

# - Использование исключений -
