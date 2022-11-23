# Простое решение

print('Введите два целых числа: ')
a = int(input())
b = int(input())
print(f'{a} + {b} = {a+b}')

# Сложное решение

a, b = map(int, input('Введите два целых числа: ').split())
print(f'{a} + {b} = {a+b}')
