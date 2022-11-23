# Простое решение

print('Введите два целых числа: ')
a = int(input())
b = int(input())
if a > b:
    print(f'{a} > {b}')
else:
    if a < b:
        print(f'{a} < {b}')
    else:
        print(f'{a} = {b}')

# Сложное решение

a, b = map(int, input('Введите два целых числа: ').split())
if a > b:
    print(f'{a} > {b}')
elif a < b:
    print(f'{a} < {b}')
else:
    print(f'{a} = {b}')
