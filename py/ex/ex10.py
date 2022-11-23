from random import randint

a = [randint(1, 6), randint(1, 6), randint(1, 6)]
print(f'Выпало очков:', *a)
b = str(a[0]) + str(a[1]) + str(a[2])
print(f'Число: {b}')
print(f'Его квадрат: {int(b) ** 2}')
