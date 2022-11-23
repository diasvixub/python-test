h, m = 8, 30
n = int(input('Введите номер урока: '))
res_m = m + (45 + 10) * n - 10
res_h = h + res_m // 60
print(f'{res_h}:{res_m % 60}')
