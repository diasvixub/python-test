a = int(input('Первый элемент a1: '))
b = int(input('Количество элементов n: '))
d = int(input('Разность d: '))

c = [0] * b

for i in range(b):
    c[i] = a + d * (b - 1)
    b -= 1

print(*c[::-1])
