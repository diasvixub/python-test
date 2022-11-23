n = int(input('Введите число: '))
k, summ = 0, 0
a = [0, 2, 4, 6, 8]

while k < n+1:
    if k % 10 in a:
        summ += k
    k += 1

print(summ)
