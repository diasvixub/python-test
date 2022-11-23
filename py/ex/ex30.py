a = [0] * 5
summ = 0

print('Массив:')

for i in range(5):
    a[i] = int(input())
    summ += a[i]

print(f'Среднее арифметическое {summ / 5}')
