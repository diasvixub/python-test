from random import randint

a = randint(100, 999)

print(f'Получено число {a}')
print(f'Сотни: {a // 100}')
print(f'Десятки: {a % 100 // 10}')
print(f'Единицы: {a % 10}')
