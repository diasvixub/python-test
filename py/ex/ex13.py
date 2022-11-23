a, b, c, d = map(int, input('Введите четыре целых числа: ').split())

if a > b and a > c and a > d:
    print('Наибольшее число', a)
elif b > a and b > c and b > d:
    print('Наибольшее число', b)
elif c > a and c > b and c > d:
    print('Наибольшее число', c)
elif d > a and d > b and d > c:
    print('Наибольшее число', d)
else:
    print('Числа равны')
