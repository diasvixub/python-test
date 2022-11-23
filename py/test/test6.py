# Простое решение

print('Введите строку: ')
a = input()
k = 0
for i in a:
    if i.isdigit():
        k = k + 1
print(k)

# Сложное решение

a = input('Введите строку: ')
k = 0
for i in a:
    if i.isdigit():
        k += 1
print(k)
