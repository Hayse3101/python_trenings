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

# ------------ Задача №21 ------------
txt = input("Введите предложение: ")
num10 = int(input("Введите отступ по индексу: "))
tuple_txt = tuple(i for i in txt)
print(f"Полученный кортеж: {tuple_txt}")
tuple_txt_index = tuple(i for i in tuple_txt if tuple_txt.index(i) % num10 == 0)
print(f"Новый кортеж, полученный из страого: {tuple_txt_index}")

# ------------ Задача №22 ------------
num2 = int(input("Введите число для формирования кортежа: "))
tuple_int = tuple(i for i in range(num2 + 1))
print(f"Созданный кортеж: {tuple_int}")
tuple_int_copy = tuple_int[:]
tuple_int_copy = sorted(tuple_int_copy)
tuple_int_copy.sort(reverse=True)
print(f"Список с перевёрнутыми значениями - {tuple_int} {tuple_int_copy}")

# ------------ Задача №23 ------------
from random import randint


def list_func(list_count_1: int, list_count_2: int):
    alphabet = [chr(i) for i in range(97, 123)]
    arr_txt1 = []
    for _ in range(list_count_1):
        for _ in range(list_count_2):
            arr_txt1.append(alphabet[randint(0, len(alphabet))])
    return arr_txt1


num11 = int(input("Введите размер списка №1: "))
num12 = int(input("Введите размер списка №2: "))
print(f"Полученные список: {list_func(num11, num12)}")

# ------------ Задача №24 ~ ------------


def gener_list(gen_list: list):
    count = 0
    for i in range(len(gen_list[0])):
        gen_list[0][i] = count
        count += 1

    for i in range(len(gen_list) - 1):
        gen_list[i + 1][len(gen_list) - 1] = count
        count += 1

    for i in range(len(gen_list[-1]) - 1):
        gen_list[-1][-2-i] = count
        count += 1

    for i in range(len(gen_list) - 2):
        gen_list[-2-i][0] = count
        count += 1

    return gen_list


num13 = int(input("Введите количество столбцов: "))
num14 = int(input("Введите количество строк: "))
list_num1 = [[0 for i in range(num13)] for j in range(num14)]
print(f"Список: {gener_list(list_num1)}")

# ------------ Задача №25 ------------
num15 = int(input("Введите количество столбцов: "))
num16 = int(input("Введите количество строк: "))
list_num2 = [[randint(0, 9) for i in range(num15)] for j in range(num16)]
print()
print(f"Список: {list_num2}")
print()
num17 = int(input("Какой столбик удалить?: "))
num18 = int(input("Какую строчку удалить?: "))

list_num2.pop(num17)
for i in range(len(list_num2)):
    del list_num2[i][num18]

print(f"Обновлённыый список: {list_num2}")

# ------------ Задача №26 ------------

arr10 = [2, 4, 1, 5, 6, 3, 0, 9, 7, 8]
print(f"Неотсортированный список: {arr10}\n")

for i in range(len(arr10)):
    for j in range(len(arr10)):
        if arr10[i] < arr10[j]:
            arr10[i], arr10[j] = arr10[j], arr10[i]

print(f"Отсортированный список: {arr10}")

# ------------ Задача №27 ------------


def list_func_2(list_1: list):
    max_value = []
    index_value = []
    for i in list_1:
        if max(list_1) == i:
            max_value.append(i)
    for i in max_value:
        index_value.append(max_value.index(i))

    print(f"Наибольший элемент(ы) - {max_value}. Индекс(ы) - {index_value}")


arr8 = [randint(0, 9) for _ in range(10)]
print(f"Список: {arr8}")
list_func_2(arr8)

# ------------ Задача №28 ------------
arr9 = [randint(0, 9) for _ in range(10)]
print(f"Список: {arr9}")

for i in arr9:
    if arr9.index(i) % 2 == 0:
        pass

# ------------ Задача №29 ------------
arr11 = [randint(0, 9) for _ in range(10)]
print(f"Список: {arr11}")

for i in range(len(arr11)):
    pass

print(f"Новый список: {arr11}")

# ------------ Задача №30 ------------
arr12 = [2, 4, 1, 7, 5, 9, 6, 8, 0, 3]
arr13 = [1, 2, 4, 5, 6, 3, 0, 9, 7, 8]
arr14 = []
count = 0

for i in arr12:
    for j in range(count, len(arr13)):
        arr14.append(i)
        arr14.append(arr13[j])
        count += 1
        break

print(f"Список: {arr14}")

# ------------ Задача №31 ------------
set_int0 = set()

for i in range(15):
    if len(set_int0) < 5:
        set_int0.add(randint(1, 10))
    else:
        set_int0.add(randint(10, 30))

print(f"Сформированое множество: {set_int0}")

# ------------ Задача №32 ------------
num19 = int(input("Введите первое число: "))
num20 = int(input("Введите второе число: "))

set_int1 = {i for i in range(num19)}
set_int2 = {i for i in range(num20)}
print(f"Составные цифры первого числа: {set_int1}")
print(f"Составные цифры второго числа: {set_int2}")
print("-------------------------------------")
print(f"Цифры. которые есть в обоих числах: {set_int1.intersection(set_int2)}")

# ------------ Задача №33 ------------
set_txt1 = set(input("Введите текст: "))
print(set_txt1)
vse_gls = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
gls_txt = {s for s in set_txt1 if s in vse_gls}

print(f"Гласные буквы в тексте: {gls_txt}")

# ------------ Задача №34 ------------
set_int3 = {n for n in range(100) if n % 3 == 0}
set_int4 = {n for n in range(100) if n % 4 == 0}

print(f"Числа которые не делятся на 3 и 4 одновременно: {set_int3 - set_int4} и {set_int4 - set_int3}")

# ------------ Задача №35 ------------
set_tuple = set()
count = 0
nums8 = [2*i+1 for i in range(20)]

for i in range(10):
    test_tuple = tuple(i for i in nums8[:2])
    nums8 = nums8[2:]
    set_tuple.add(test_tuple)

print(f"Множество с кортежами: {set_tuple}")

# ------------ Задача №36 ------------
num21 = int(input("Введите число: "))

if num21 < 0:
    num21 *= -1

list_int1 = [i for i in range(1, num21 + 1)]
dict_1 = {list_int1[i]: list_int1[-i - 1] for i in range(len(list_int1))}

print(f"Сформированны словарь: {dict_1}")

# ------------ Задача №37 ------------
value_txt1 = input("Введите текст: ")
count2 = 0
set_txt2 = {i for i in value_txt1}
dict_txt1 = {i: 0 for i in set_txt2}

for i in value_txt1:
    if i in dict_txt1:
        dict_txt1[i] += 1

print(f"Разделение по буквам: {dict_txt1}")

# ------------ Задача №38 ------------
list_txt1 = [input("Введите фамилию авторов: ") for _ in range(int(input("Сколько авторов вы хатите ввести: ")))]
dict_txt2 = {list_txt1[i]: input(f"Произведение автора {list_txt1[i]}: ") for i in range(len(list_txt1))}

print(f"Готовый словарь: {dict_txt2}")

# ------------ Задача №39 ------------
txt_value1 = input("Введите текстовое значение: ")
set_txt3 = {i for i in txt_value1}
dict_txt2 = {i: '' for i in set_txt3}

for i in dict_txt2.keys():
    for j in txt_value1:
        if i != j:
            dict_txt2[i] += j

print(f"Созданный словарь: {dict_txt2}")

# ------------ Задача №40 ~ ------------
dict_num1 = {i: i*2+1 for i in range(10)}
dict_num2 = {i: i**2 for i in range(10)}

print(f"Готовы словарь: {dict_num1}, {dict_num2}")

# ------------ Задача №41 ------------
txt_input1 = input("Введите текст: ")
remove_txt1 = txt_input1.replace("*", " Hello Python ")
print(remove_txt1)

for i in txt_input1:
    if i == '*':
        print("Hello Python")

# ------------ Задача №42 ------------
txt_input2 = input("Введите текст: ")
remove_txt2 = txt_input2.replace("*", "A")
print(remove_txt2)

for i in txt_input2:
    if i == '*':
        print("A")

# ------------ Задача №43 ------------
txt_input3 = input("Введите текст: ")
txt_value2 = ""

for i in txt_input3:
    if i == i.lower():
        txt_value2 += i.upper()
    else:
        txt_value2 += i.lower()

print(f"Полученный текст: {txt_value2}")

# ------------ Задача №44 ------------
txt_input4 = input("Введите текст: ")
txt_list1 = "".join(txt_input4)
new_txt_value1 = ""

for i in range(len(txt_input4)):
    if i + 2 > len(txt_input4) - 1:
        new_txt_value1 += txt_list1[1]
        new_txt_value1 += txt_list1[0]
        break
    else:
        new_txt_value1 += txt_list1[i + 2]

print(f"Полученный текст: {new_txt_value1}")

# ------------ Задача №45 ------------
txt_input5 = input("Введите первый текст: ")
txt_input6 = input("Введите второй текст: ")
new_txt_value2 = ""

list_txt2 = ''.join(txt_input5)
list_txt3 = ''.join(txt_input6)

max_len_txt = None
min_len_txt = None

if len(list_txt2) > len(list_txt3):
    max_len_txt = list_txt2
    min_len_txt = list_txt3
else:
    max_len_txt = list_txt3
    min_len_txt = list_txt2

for i in max_len_txt:
    count = 0
    new_txt_value2 += i
    if count <= len(min_len_txt):
        for j in min_len_txt:
            new_txt_value2 += j
            count += 1
            break
    min_len_txt = min_len_txt[count:]
else:
    new_txt_value2 += '*'

print(f"Полученный текст: {new_txt_value2}")

# ------------ Задача №46 ------------

