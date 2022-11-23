a = input('Введите число: ')
count = 0

for i in a:
    if i != '0' and i != '1':
        count += 1

if count > 0:
    print('Нет.')
else:
    print('Да.')
