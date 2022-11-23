# Простое решение

from random import randint

a = [0] * 10
summ = 0

for i in range(10):
    a[i] = randint(1, 100)

for i in a:
    if i % 2 == 0:
        summ += i

print(*a)
print(summ)

# Сложное решение

from random import randint

a = [0] * 10
summ = 0

for i in range(10):
    a[i] = randint(1, 100)
    if a[i] % 2 == 0:
        summ += a[i]

print(*a)
print(summ)
