from random import randint

a = [randint(1, 6), randint(1, 6), randint(1, 6)]
print(f'Выпало очков:', *a)
print(f'({a[0]} + {a[1]} + {a[2]}) / 3 = {(a[0] + a[1] + a[2]) / 3}')
