# Простое решение

print('Введите три числа:')
a = int(input())
b = int(input())
c = int(input())
print(f'{a} + {b} + {c} = {a + b + c}')

# Сложное решение

a, b, c = map(int, input('Введите три числа: ').split())
print(f'{a} + {b} + {c} = {a + b + c}')
