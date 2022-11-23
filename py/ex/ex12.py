a, b = map(int, input('Введите два целых числа: ').split())

if a > b:
    print(f'Наибольшее число {a}')
    print(f'Наименьшее число {b}')
else:
    print(f'Наибольшее число {b}')
    print(f'Наименьшее число {a}')
