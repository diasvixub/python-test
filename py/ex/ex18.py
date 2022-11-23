a = input('Введите имя файла: ')
web = ['htm', 'html', 'php']

if a[-4:] in web or a[-3:] in web:
    print('Это веб-страница!')
else:
    print('Что-то другое.')
