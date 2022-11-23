k, n = map(int, input('Введите два числа: ').split())
summ = 0
a = [1, 3, 5, 7, 9]

while k < n+1:
    if k % 10 in a:
        summ += k
    k += 1

print(summ)
