a = int(input('Введите натуральное число: '))
count = 0

while a > 10:
    b = a % 100
    if b // 10 == b % 10:
        count += 1
        a //= 10
    else:
        a //= 10

if count > 0:
    print('Да.')
else:
    print('Нет.')
