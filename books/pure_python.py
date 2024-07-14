# ------------------------------------ 2 Шаблоны для чистого python -----------------------------------
# ----------------------------- 2.1. Прикрой свой з** инструкциями assert -----------------------------
import threading


def apply_discount(product, discount):
    price = int(product['цена'] * (1.0 - discount))
    """ Assert проверяте правильность утверждения
     Если утверждение True, то ничего не происходит. Но если же условие False,
      то вызывается исключение AssertionError """
    assert 0 <= price <= product['цена']

    return price


shoes = {'имя': 'Модные туфли', 'цена': 14900}
apply_discount(shoes, 0.25)

# Assert это средство отладки
# инструкция_assert ::= "assert" выражени1 ["," выражение2]
# Выражение1 - это условие, которое надо проверить, а вырожение 2 - это сообщение об ошибке, которое выводится на экран

"""
if __debug__:
    if not Выражение1:
        raise AssertionError(Выражение2)
"""


# -------- Предостережения Assert --------
# ------------------ 1 -------------------


def delete_product1(prod_id, user):
    """ Если утверждения assert отключены в интерператоре Python
    Как не стоит использовать assert"""
    assert user.is_admin(), 'здесь должент быть администратор'  # <- Непрвильное использование assert
    assert store.has_product(prod_id), 'Неизвестный продукт'  # <- Неправильное использование assert
    store.get_prodect(prod_id).delete()


def delete_product2(product_id, user):
    """ Правильное написание функции, без использования assert """
    if not user.is_admin():
        raise AuthError("Для удалениян необходимы права админа")
    if not store.has_product(product_id):
        raise ValueError('Индетификатор неизвестного товара')
    store.get_prodect(prod_id).delete()


# ------------------ 2 -------------------
assert (1 == 2, 'Это утверждение должно вызвать сбой')  # <- Но сбоя не будет, так как утверждение будет True
#  В Python, пустыне кортежи всегда являются истинными

# --------------------------------- 2.2. Беспечное размещение зяпятой ---------------------------------
names1 = ['Элис', 'Боб', 'Дилберт']  # <- Могут возникнуть трудности при просмотре командой git diff

names2 = ['Элис',  # <- Болле правильное размещения, для более удобного просмотра с git diff
          'Боб',
          'Дилберт'  # <- Отсутствие запятой, может добавить трудностей с добавление нового элемента
          ]

names3 = ['Элис',
          'Боб',
          'Дилберт'  # <- Из-за отсутствия запятой, может произойти слияние элементов ['Элис', 'Боб', 'ДилбертДжейн']
          'Джейн'
          ]

# Нужно не забывать всегда заканчивать строки запятой
names4 = ['Элис',
          'Боб',
          'Дилберт',
          'Джейн',  # <- Лишней запятая не будет
          ]

# ----------------------------- 2.3. Менеджеры контекста и инструкция with ----------------------------
with open('hello.txt', 'w') as f:
    f.write('привет, мир!')

# Код ниже представляет код выше на внутреннем уровне
f = open('hello.txt', 'w')
try:
    f.write('привет, мир!')
finally:
    f.close()

# Ещё один пример инструкции with
some_lock = threading.Lock()

# Вредно:
some_lock.acquire()
try:
    pass  # Сделать что-то
finally:
    some_lock.release()

# Полезно:
with some_lock:
    pass  # Сделать что-то

# ---- Поддержка конструкции with в собственныз объектах ----
# Пример контекстного менеджера open()


class ManagesFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagesFile('hello.txt') as f:
    f.write('привет, мир!')
    f.write('а теперь, пока!')

# ---- Написание красивыйх API с менеджером контекста ----


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)



with Indenter() as indent:
    indent.print('привет!')
    with indent:
        indent.print('здорово')
        with indent:
            indent.print('бонжур')
    indent.print('эй')

# ----------------------------- 2.4. Подчёркивания, дендеры и другое ----------------------------
# ---- 1. Одинарный начальный символ подчёркивания: _var ----


class Test_1:
    def __init__(self):
        self.foo = 11
        self._bar = 23


# ---- 2. Одинарный замыкающий символ подчёркивания: var_ ----

"""
def make_object(name, class):
 -> SyntaxError: "invalid syntax"
"""

def make_object(name, class_):
    pass


# ---- 3. Двойной начальный символ подчёркивания: __var ----

class Test_2:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23  # <- _Test__baz


t = Test_1()
dir(t)


class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        self.__method()

# ---- 4. Двойной начальный и замыкающий символ подчёркивания __var__ ----

