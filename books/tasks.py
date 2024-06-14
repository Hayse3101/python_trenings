# -------------------- Задачи предоставленные в книгах --------------------
import datetime
import random
from datetime import date
from fractions import Fraction

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
        gen_list[-1][-2 - i] = count
        count += 1

    for i in range(len(gen_list) - 2):
        gen_list[-2 - i][0] = count
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
nums8 = [2 * i + 1 for i in range(20)]

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
dict_num1 = {i: i * 2 + 1 for i in range(10)}
dict_num2 = {i: i ** 2 for i in range(10)}

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

max_len_txt += "*"
min_len_txt += "*"

for i in max_len_txt:
    count = 0
    new_txt_value2 += i
    if count <= len(min_len_txt):
        for j in min_len_txt:
            new_txt_value2 += j
            count += 1
            break
    min_len_txt = min_len_txt[count:]

print(f"Полученный текст: {new_txt_value2}")

# ------------ Задача №46 ------------
txt_input7 = input("Введите текст: ")
encoded_txt1 = txt_input7
letter_value1 = txt_input7[:1]
encoded_txt1 = encoded_txt1[1:] + letter_value1

decrypted_txt1 = letter_value1 + encoded_txt1[:len(encoded_txt1) - 1]

print(f"Зашифрованное значение: {encoded_txt1}")
print(f"Расшифрованное значение: {decrypted_txt1}")

# ------------ Задача №47 ------------
txt_input8 = input("Введите текст: ")
encoded_txt2 = txt_input8
letters_value1 = encoded_txt2[len(txt_input8) - 2:]
encoded_txt2 = letters_value1 + encoded_txt2[:-2]

decrypted_txt2 = encoded_txt2[2:] + letters_value1

print(f"Зашифрованное значение: {encoded_txt2}")
print(f"Расшифрованное значение: {decrypted_txt2}")

# ------------ Задача №48 ~ ------------
txt_input9 = input("Введите текст: ")
list_txt4 = [i for i in txt_input9]
letters_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
letters_sgls = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п',
                'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', ]

new_txt_value3 = ""

first_gls = ""
first_sgls = ""
second_gls = ""
second_sgls = ""

for i in list_txt4:
    pass

print(f"Рузльтат шифровки: {new_txt_value3}")

# ------------ Задача №49 ------------
txt_input10 = input("Введите текст: ")
list_words1 = txt_input10.split()
max_word = ""
min_word = ""

for word in list_words1:
    if len(word) > len(max_word):
        max_word, min_word = word, max_word

    if len(word) < len(min_word):
        min_word = word

list_words1.remove(max_word)
list_words1.remove(min_word)
new_txt_value3 = " ".join(list_words1)

print(f"Новый текст: {new_txt_value3}")

# ------------ Задача №50 ------------
txt_input11 = input("Введите текст: ")
list_words2 = txt_input11.split()
revers_list_words2 = []

for word in list_words2:
    revers_list_words2.append(word[::-1])

new_txt_value3 = " ".join(revers_list_words2)

print(f"Новый текст: {new_txt_value3}")


# ------------ Задача №51 ------------


def func3(arr_one: list, arr_two: list):
    mult_value = 0
    sum_value = 0
    if len(arr_one) > len(arr_two):
        diff_value = len(arr_one) - len(arr_two)
        arr_two += [arr_one[i] for i in range(diff_value)]
    else:
        diff_value = len(arr_two) - len(arr_one)
        arr_one += [arr_two[i] for i in range(diff_value)]

    for i in range(len(arr_one)):
        mult_value = arr_one[i] * arr_two[i]
        sum_value += mult_value

    return sum_value


print(f"Рузультат работы функции: {func3([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])}")


# ------------ Задача №52 ------------


def func4(arr: list) -> list:
    return [i for i in arr if i % 2 == 0]


print(f"Рузультат работы функции: {func4([i for i in range(10)])}")


# ------------ Задача №53 ------------


def func5(*args):
    yield sum(args) / 2
    yield max(args)
    yield min(args)


for i in func5(4, 2, 3, 1, 7, 8, 9, 0, 2, 3, 5, 67, 123, 2):
    print(f"Полученные значения: {i}", end=" ")


# ------------ Задача №54 ~ ------------


def func6(txt_value: str, *int_value):
    sorted_int = list(int_value)
    sorted_int.sort()
    result_txt = {key: value for key, value in zip(txt_value, sorted_int)}

    return result_txt


print(f"Рузльтат: {func6("Hello World", 0, 2, 1, 4, 5, 6, 8, 3, 9, 7, 10, 11)}")


# ------------ Задача №55 ------------


def func7(func, value_int_1, value_int_2):
    int_value = randint(value_int_1, value_int_2)
    func(int_value)


def func8(value_int_1, value_int_2):
    global max_value

    if value_int_1 > value_int_2:
        max_value = value_int_1


max_value = 0
count3 = int(input("Сколько чисел вводить?: "))
for i in range(count3):
    print(f"Наибольшое число {func7(func8, 10, 50)}")


# ------------ Задача №56 ------------


def func9(func, num: int):
    for n in range(num):
        if n % 2 == 0:
            func(n)


def func10(num: int):
    global int_value

    int_value += num


int_value = 0
func9(func10, 10)
print(f"Сумма четных значений: {int_value}")


# ------------ Задача №57 ------------


def func11(txt_value: str):
    if len(txt_value) == 0:
        return
    else:
        letter_value2 = txt_value[:1]

        print(f"Буква: {letter_value2}")
        func11(txt_value[1:])


func11("Hello World")


# ------------ Задача №58 ------------


def func12(value: int, factor: int, flag: int):
    if flag == 0:
        return value
    else:
        print(f"{factor} * {value} = {factor * value}")
        value = factor * value
        return func12(value, factor, flag - 1)


func12(1, 3, 10)


# ------------ Задача №59 ------------


def func13(num: int):
    for i in range(num):
        yield input("Введите месяц: ")


count_month = int(input("Сколько месяцев Вы знаете?: "))
print(f"Месяца: {func13(count_month)}")


# ------------ Задача №60 ------------


def func14(num: int):
    for i in range(num):
        yield 2 ** i


num22 = int(input("Количетсов степеней двойки: "))
print(f"Степени двойки - {list(func14(num22))}")


# ------------ Задача №61 ------------


def convert_to(num, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result.upper() if upper else result


notation, number1 = int(input("Введите систему счисления: ")), input("Введите число: ")
print(f"Результат перевода: {convert_to(notation, number1)}")

# ------------ Задача №62 ------------
bit, int_number = int(input("Введите номер бита: ")), int(input("Введите целое число: "))

binary_number = "{0:b}".format(bit)
if bit not in range(len(binary_number)):
    print("Invalid input")
else:
    print(binary_number, binary_number[bit])

# ------------ Задача №63 ------------
int_value1 = int(input("Введите число: "))
binary_translation = bin(int_value1)
binary_representation = str(binary_translation[2:])
bit_sum = 0

for bit in binary_representation:
    sum += int(bit)

print(f"Сумма значений всех битов: {bit_sum}")

# ------------ Задача №64 ------------
int_value2 = int(input("Введите целое число: "))
oct_value = str(oct(int_value2)[2:])
list_oct_value = list(oct_value)
random.shuffle(list_oct_value)
new_oct_value = ''
for num in list_oct_value:
    new_oct_value += num

print(f"Полученное число: {oct_value}")
print(f"Измененаый порядок: {new_oct_value}")

# ------------ Задача №65 ------------
numerator1 = int(input("Введите числитель 1: "))
numerator2 = int(input("Введите числитель 2: "))
denominator1 = int(input("Введите знаменатель 1: "))
denominator2 = int(input("Введите знаменатель 2: "))

rational_fraction_one = Fraction(numerator1, denominator1)
rational_fraction_two = Fraction(numerator2, denominator2)

result_list1 = [rational_fraction_one + rational_fraction_two, rational_fraction_one - rational_fraction_two,
                rational_fraction_one * rational_fraction_two, rational_fraction_one / rational_fraction_two]

print(f"Максимальное значение: {max(result_list1)}")
print(f"Минимальное значение: {min(result_list1)}")

# ------------ Задача №66 ------------
int_a1 = int(input("Введите a1: "))
int_a2 = int(input("Введите a2: "))
int_b1 = int(input("Введите b1: "))
int_b2 = int(input("Введите b2: "))

complex_number_one = complex(int_a1, int_b1)
complex_number_two = complex(int_a2, int_b2)

result_list2 = [abs(complex_number_one + complex_number_two), abs(complex_number_one - complex_number_two),
                abs(complex_number_one * complex_number_two), abs(complex_number_one / complex_number_two)]

print(f"Максимальное значение: {max(result_list2)}")
print(f"Минимальное значение: {min(result_list2)}")

# ------------ Задача №67 ------------
date_user_one = input("Введите первую дату: ")
date_user_two = input("Введите вторую дату: ")

date_one = date.fromisoformat(date_user_one)
date_two = date.fromisoformat(date_user_two)
day_difference = (date_one - date_two).days

print(f"Колличество полных дней между датами: {day_difference}")

# ------------ Задача №68 ------------
user_time_str = input("Введите время: ")
user_time_onj = datetime.datetime.strptime(user_time_str, '%Y-%m-%d %H:%M:%S.%f')
current_time = datetime.datetime.now().time()

print(f"Интервал времени: {user_time_onj.time() - current_time}")

# ------------ Задача №69 ------------
name_file = input("Введите имя файла: ")
user_file = open(name_file + ".txt")
new_txt_file = open("test.txt")
k = 1
for line in user_file:
    new_line = f"[{str(k)}] - line"
    new_txt_file.write(new_line)
    k += 1

user_file.close()
new_txt_file.close()
# ------------ Задача №70 ------------
user_name_file = input("Введите имя файла: ")
count_line = int(input("Введите колличество строк: "))
content_user_file = [input("Строчка: ") for _ in range(count_line)]

new_user_file = open(user_name_file + ".txt", 'x')
k = 1
for line in content_user_file:
    new_user_file.write(line.swapcase())
    k += 1

new_user_file.close()


# ------------ Задача №71 ------------


class TestClass2:
    def __init__(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two
        print(f"Поля созданы")

    def show_value(self):
        print(f"Первое поле: {self.value_one}")
        print(f"Второе поле: {self.value_two}")


test_obj = TestClass2("Hello", "World")
test_obj.show_value()


# ------------ Задача №72 ------------


class TestClass2:
    def __init__(self, value_one, value_two):
        if type(value_one) == str and type(value_two) == str:
            self.txt_value = value_one + value_two
            print("Поле создано")
        elif type(value_one) == int and type(value_two) == int:
            self.int_value = value_one + value_two
            print("Поле создано")
        else:
            self.error = "Значения разные!"

    def display_methods(self):
        if hasattr(self, 'txt_value'):
            print(f"Полученный текст: {self.txt_value}")
        elif hasattr(self, 'int_value'):
            print(f"Полученное число: {self.int_value}")
        else:
            print("Поля отсутствуют")


test_obj_txt = TestClass2("Hello ", "World")
test_obj_int = TestClass2(5, 5)
test_obj_int_and_txt = TestClass2("Hello", 10)

test_obj_txt.display_methods()
test_obj_int.display_methods()
test_obj_int_and_txt.display_methods()


# ------------ Задача №73 ------------


class TestClass3:
    def __init__(self, value_list: list):
        fields_int_list = []

        for value in value_list:
            if type(value) == int:
                fields_int_list.append(value)

        self.fields_int_list = fields_int_list

    def display_fields_int_list(self):
        for value in range(len(self.fields_int_list)):
            print(f"[{value}] {self.fields_int_list[value]}")

    def list_average(self):
        print(f"Среднее значение списка: {sum(self.fields_int_list) / len(self.fields_int_list)}")


test_obj_list_int = TestClass3([1, 3, 4, 5, 2, 8, 7, 9, 10])
test_obj_list_int_str = TestClass3([1, 4, 6, 't', 6, 'h', 'q', 8])

test_obj_list_int.display_fields_int_list()
test_obj_list_int.list_average()

test_obj_list_int_str.display_fields_int_list()
test_obj_list_int_str.list_average()


# ------------ Задача №74 ------------


def func_create_obj1(list_str: list, name_class: str):
    class TestClass4:
        def __init__(self):
            value_namber = 0
            for value in list_str:
                if type(value) == str:
                    self.value = value_namber
                    value_namber += 1

        def display_fields(self):
            for value in dir(self):
                if not value.startswith("_") and value != "display_fields":
                    print(f"{value} = {self.__dict__[value]}")

    TestClass4.__name__ = name_class
    return TestClass4


test_obj_list_str = func_create_obj1(["hello", "world", "puthon"], "TestClass")
test_obj_list_str.display_fields()
# ------------ Задача №75 ------------


def func_create_obj2(finished_obj, new_obj):
    new_obj = finished_obj

    return new_obj


class TestClass5:
    def __init__(self, value_str):
        self.hello = value_str

    def display(self):
        print(f"Приветсвие: {self.hello}")


test_obj_hello = TestClass5("Hello")
name_new_test_obj = None
new_test_obj = func_create_obj2(test_obj_hello, name_new_test_obj)
new_test_obj.display()
