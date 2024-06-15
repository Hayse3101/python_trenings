def func_create_list_name_objs(num_obj: int):
    name_obj = ''
    for n in range(num_obj):
        name_obj = "obj_" + str(n)
        yield name_obj


def func_create_obj3(name_obj: str):
    class TestClass6:
        odd_number = None

        def input_odd_number(self):
            self.odd_number = int(input("Ввдеите нечетное число:"))

            if self.odd_number % 2 == 0:
                self.odd_number = "четное"
                print(f"Ввденое число ялвяется четным")
            else:
                print(f"Добавлено число: {self.odd_number}")

    TestClass6.__name__ = name_obj
    return TestClass6


number_obj = int(input("Сколько будеть создано объектов: "))
name_obj_list = []
list_obj = []

for name in func_create_list_name_objs(number_obj):
    name_obj_list.append(name)

for name in name_obj_list:
    list_obj.append(func_create_obj3(name))

print(f"Список объектов: {list_obj}")
