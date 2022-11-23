from random import randint

a, b = map(int, input('Введите границы диапазона: ').split())
c = [0] * 10

for i in range(10):
    if a < b:
        c[i] = randint(a, b)
    else:
        c[i] = randint(b, a)

print(*c)
