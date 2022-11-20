# Уроки

1. [Установка](#Установка)
    - [Установка Python](#Установка-Python)
    - [Установка IDE PyCharm](#Установка-IDE-PyCharm)
2. [Синтаксис](#Синтаксис)
3. [Ветвление](#Ветвление)
4. [Циклы](#Циклы)
5. [Списки (массивы)](#Списки)
6. [Импорт библиотек](#Импорт-библиотек)

---

## Установка

Чтолбы использовать возможности Python, необходимо установить его в систему или использовать стороннюю IDE.
В наших уроках мы будем использовать IDE **PyCharm Community** от *JetBrains*. Вы же можете использовать как поставляемый с Python редактор кода,
так и используемую в уроках IDE или даже онлайн компилятор Python [replit](https://replit.com/languages/python3).

### Установка Python

Заходим на [официальный сайт](https://www.python.org) и наводим курсор на **Downloads** как показано на скриншоте ниже.

![Сайт Python.org](https://github.com/diasvixub/python-test/blob/main/img/screen-1.png)

Находим кнопку **Python 3.x.x** и нажимаем на нее. На момент написания статьи последняя версия **Python 3.11.0**.

![Кнопка скачивания](https://github.com/diasvixub/python-test/blob/main/img/screen-2.png)

Обратите внимание, что **Python 3.9 и выше** не поддерживается на ОС Windows 7. Если у вас ОС Windows 7 или ниже, установите **Python 3.8 или ниже**, перейдя по [ссылке](https://www.python.org/downloads) и пролистнув страницу вниз до заголовка **Looking for a specific release?**.

![Старые версии Python](https://github.com/diasvixub/python-test/blob/main/img/screen-3.png)

После загрузки нужной версии, откройте файл **python-3.x.x-amd64.exe**.

![Установщик Python](https://github.com/diasvixub/python-test/blob/main/img/screen-4.jpg)

Поставьте галочку напротив пункта **Add python.exe to PATH** и нажмите на кнопку **🛡️Install Now**.

Дождитесь завершения установки.

![Завершение установки Python](https://github.com/diasvixub/python-test/blob/main/img/screen-5.jpg)

Готово! Python установлен на ваш компьютер.

Чтобы в этом убедится, запустите командную строку (**Win + R** и введите в поле *Открыть:* **cmd**) и введите **python**.
Если установка прошла успешно, в командной строке покажется версия установленного Python.

![Проверка Python](https://github.com/diasvixub/python-test/blob/main/img/screen-6.jpg)

Теперь для написания программ на Python вам нужно найти в **меню ПУСК** программу **IDLE (Python 3.x.x 64-bit)** и запустить ее. Вам откроется интерактивный режим Python.

![Интерактивный режим Python](https://github.com/diasvixub/python-test/blob/main/img/screen-7.jpg)

Чтобы открыть редактор кода, необходимо нажать на вкладку **File** вверху окна и выбрать пункт **New File**.

![Редактор кода Python](https://github.com/diasvixub/python-test/blob/main/img/screen-8.jpg)

Вуаля! Перед вами редактор кода, который поставляется вместе с Python.
В нем вы можете писать свои программы и сразу же их запускать нажав на клавишу **F5** или выбрав пункт **Run Module** во вкладке **Run** вверху окна, перед этим сохранив файл.

После сохранения файла с расширением **.py** редактор кода начнет подсвечивать синтаксис.

### Установка IDE PyCharm

Переходим на [официальный сайт PyCharm](https://www.jetbrains.com/pycharm/) и нажимаем кнопку **Download**.

![Официальный сайт PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-9.png)

Тут нас интересует версия Community. Нажимаем **Download**.

![Скачивание PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-10.png)

Обратите внимание, что последняя версия поддерживаемая ОС Windows 7 это **PyCharm 2019.3.x**. Поэтому, если у вас ОС Windows 7, скачайте **PyCharm 2019.3.x** или более позднюю версию по [ссылке](https://www.jetbrains.com/pycharm/download/other.html).

![Старые PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-11.png)

После загрузки, откройте файл **pycharm-community-20**.*.*.exe**.

Жмем везде **Next**. Ставим галочки напротив **.py** и **PyCharm Community Edition**, если вам нужен ярлык на рабочем столе.

![Установка PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-12.png)

После завершения установки запустите PyCharm с помощью ярлыка на рабочем столе или из меню пуск.

![Интерфейс PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-13.png)

Нажмите **New Project** чтобы создать новый проект или **Open**, чтобы открыть существующий проект.

Выберите директорию проекта и нажмите **Create**.

*Под проектом понимается директория (папка), в которой хранится код ваших программ и файлы, необходимые для работы программы.*

Откроется окно проекта. Слева - файлы проекта, слева - редактор кода.

![Окно проекта PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-14.jpg)

Нажмите правой кнопкой по папке с названием вашего проекта и наведите курсор на **New**.

![Создание файла PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-15.jpg)

В выпадающем списке выберите **Python File** и введите его название, например, **main,py**.

В редакторе кода откроется созданный файл. Введите туда следующий код:

`print('Hello World!')`

![Hello World PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-16.jpg)

Чтобы запустить код, нажмите сочетание клавишь **Shift + F10** или нажмите на зеленый треугольник в правом верхнем углу окна.

![Run PyCharm](https://github.com/diasvixub/python-test/blob/main/img/screen-17.png)

Внизу окна откроется консоль с выводом программы. Там же будут выводится ошибки программы, если таковые будут.

На этом установка Python завершена. Что использовать в будущем зависит только от вас. Рекомендую использовать PyCharm, так как в нем более удобно работать в отличии от других IDE. 

## 
