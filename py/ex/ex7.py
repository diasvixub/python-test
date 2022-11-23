time = int(input('Число секунд: '))
h = time // 3600
m = (time - h * 3600) // 60
s = (time - h * 3600 - m * 60) % 60
print(f'{h} ч. {m} мин. {s} с.')
