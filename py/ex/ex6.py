# Простое решение

print('Стоимость пирожка:')
a, b = map(int, input().split())
print('Сколько пирожков:')
c = int(input())
rub = a * c + b * c // 100
kop = b * c % 100
print(f'К оплате: {rub} руб. {kop} коп.')

# Сложное решение

a, b = map(int, input('Стоимость пирожка: ').split())
c = int(input('Сколько пирожков: '))
print(f'К оплате: {a * c + b * c // 100} руб. {b * c % 100} коп.')