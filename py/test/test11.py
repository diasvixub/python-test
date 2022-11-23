# Простое решение

from random import randint

a = [0] * 10
summ = 0
count = 0

for i in range(10):
    a[i] = randint(10, 100)

for i in a:
    if i % 10 == 5:
        summ += i
        count += 1

print(*a)

if count > 0:
    print(summ / count)
else:
    print('Таких элементов нет.')

# Сложное решение

from random import randint

a = [0] * 10
summ = 0
count = 0

for i in range(10):
    a[i] = randint(10, 100)
    if a[i] % 10 == 5:
        summ += a[i]
        count += 1

print(*a)

if count > 0:
    print(summ / count)
else:
    print('Таких элементов нет.')
