# Простое решение

print('Введите целое число: ')
n = int(input())
k = 0
while n > 0:
    n = n // 10  # Отсекаем последнюю цифру
    k = k + 1    # Увеличиваем счетчик
print(k)

# Сложное решение

n = int(input('Введите целое число: '))
k = 0
while n > 0:
    n //= 10  # Отсекаем последнюю цифру
    k += 1    # Увеличиваем счетчик
print(k)
