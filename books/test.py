shoes = {'имя': 'Модные туфли', 'цена': 14900}
price = int(shoes['цена'] * (1.0 - 0.25))
test = 0 <= price <= shoes['цена']
print(test)
