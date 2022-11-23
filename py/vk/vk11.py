a, b, c = map(int, input('Введите три числа: ').split())

if a + b == c or a + c == b or b + c == a:
    print('ДА')
