a, b, c = map(int, input('Введите три числа: ').split())

if a == b or b == c or a == c:
    print('ДА')
else:
    print('ERROR')
