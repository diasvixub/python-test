n = int(input('Введите размер массива: '))
a = [1] * n

for i in range(2, n):
    a[i] = a[i-2] + a[i-1]

print(f'Числа Фибоначчи:', *a)
