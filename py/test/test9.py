# Простое решение

from random import randint

a = [0] * 10
count = 0

for i in range(10):
    a[i] = randint(175, 195)

for i in a:
    if i > 180 and i < 190:
        count += 1

print(*a)
print(count)

# Сложное решение

from random import randint

a = [0] * 10
count = 0

for i in range(10):
    a[i] = randint(175, 195)
    if 180 < a[i] < 190:
        count += 1

print(*a)
print(count)
