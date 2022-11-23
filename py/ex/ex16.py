age = int(input('Введите возраст: '))

if 10 < age < 15:
    print(f'Вам {age} лет.')
elif age % 10 == 1:
    print(f'Вам {age} год.')
elif 1 < age % 10 < 5:
    print(f'Вам {age} года.')
else:
    print(f'Вам {age} лет.')
