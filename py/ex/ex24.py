a = input('Введите строку: ')
b = a.split()
c = ''

for i in range(len(b)):
    c += b[i]

print(c)
