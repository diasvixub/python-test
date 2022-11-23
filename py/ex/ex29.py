from random import randint

a, b = map(int, input('Введите границы диапазона: ').split())
c = [0] * 10

for i in range(5):
    if a < b:
        c[i] = randint(a, b)
        c[i+5] = c[i] ** 2
    else:
        c[i] = randint(b, a)
        c[i+5] = c[i] ** 2

print(*c)
