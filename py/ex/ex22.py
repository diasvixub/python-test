a = input('Введите число: ')
b, c = 0, 0

for i in a:
    if i == '0':
        b += 1
    if i == '1':
        c += 1

print(f'Нулей: {b}')
print(f'Единиц: {c}')
