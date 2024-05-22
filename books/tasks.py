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
