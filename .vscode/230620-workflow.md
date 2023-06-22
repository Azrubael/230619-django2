2023-06-20  20:45
=================

# Установка виртуальной среды
    $ python -m venv my_env

# Активация виртуальной среды
    $ source my_env/bin/activate

# Установка фреймворка Django
    $ pip install Django~=4.1.0
    $ python -m django --version
4.1.9

# Создание проекта Django с именем mysite
    $ django-admin startproject mysite

# В дальнешем следует применить нижеуказанную команду для формирования перечня зависимостей проекта, который выкладывается на GitHub
    $ python -m pip freeze > requirements.txt
# Ссылка на офифиальную документацию: https://pip.pypa.io/en/stable/cli/pip_freeze/
    $ pip install -r requirements.txt
# Если нужно быстро восстановить зависимости


(my_env)$ cd mysite
(my_env)$ python ./mysite/manage.py migrate
# это применяемые веб-фреймворком Django миграции базы данных. В результате применения изначальных настроек в базе данных создаются таблицы для приложений, перечисленных в на строечном параметре INSTALLED_APPS.
# При применении миграций, Django будет создавать таблицу по каждой модели, определенной в файле models.py приложения.
    
    
# Запуск сервера разработки
(my_env)$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
June 20, 2023 - 18:27:13
Django version 4.1.9, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

# Сервер разработки можно выполнять на конкретно-прикладном хосте и порту либо сообщать Django, что нужно загружать определенный настроечный файл, как показано ниже:
(my_env)$ python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings
    
    
=======================================================================
# Создаем приложение 'blog'
(my_env)$ python manage.py startapp blog
    $ cd ..
    $ tree -alL 4
.
├── my_env
│   ├── bin
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── Activate.ps1
│   │   ├── django-admin
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.10
│   │   ├── python -> /usr/bin/python
│   │   ├── python3 -> python
│   │   ├── python3.10 -> python
│   │   └── sqlformat
│   ├── include
│   ├── lib
│   │   └── python3.10
│   │       └── site-packages
│   ├── lib64 -> lib  [recursive, not followed]
│   └── pyvenv.cfg
├── mysite
│   ├── blog                << приложение 'blog'
│   │   ├── admin.py
│   │   ├── apps.py         << содержит главную конфигурацию приложения 'blog'
│   │   ├── __init__.py
│   │   ├── migrations      << миграции базы данных
│   │   │   └── __init__.py
│   │   ├── models.py       << относимые к приложению модели данных, м/б пустым
│   │   ├── tests.py
│   │   └── views.py        << логика приложения
│   ├── db.sqlite3
│   ├── manage.py
│   └── mysite              << это пакет проекта на языке Python
│       ├── asgi.py         << конфигурация проекта как приложения, работающего по протоколу интерфейса шлюза асинхронного сервера (ASGI)
│       ├── __init__.py
│       ├── __pycache__
│       ├── settings.py     << параметры и конфигурация проекта, содержит конфигурацию базы данных проекта в настроечном параметре DATABASES
│       ├── urls.py         << шаблоны URL-адресов
│       └── wsgi.py         << конфигурация проекта как приложения, работающего по протоколу интерфейса шлюза веб-сервера (WSGI)
└── .vscode
    └── 230620-workflow.md

13 directories, 32 files

    $ vim ../misite/blog/models.py
    
    
# Активация приложения 'blog' (стр.47)
========================================
    $ 
