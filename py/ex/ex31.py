from random import randint

a = [0] * 10
summ1, summ2, c1, c2 = 0, 0, 0, 0

for i in range(10):
    a[i] = randint(0, 100)
    if a[i] < 50:
        summ1 += a[i]
        c1 += 1
    if a[i] >= 50:
        summ2 += a[i]
        c2 += 1

print(*a)
print(f'Ср. арифм. элементов < 50: {summ1 / c1}')
print(f'Ср. арифм. элементов >= 50: {summ2 / c2}')
