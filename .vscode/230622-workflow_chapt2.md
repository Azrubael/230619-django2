# 2023-06-21  15:52
===================

# Продвинутые функциональности
==============================
[стр.80]
# Если нужно быстро восстановить зависимости
    $ pip install -r dependencies.txt
# Активация виртуальной среды
    $ source my_env/bin/activate
# Запуск сервера разработки
(my_env)$ python ./mysite/manage.py runserver

# Добавил иконку для приложения
    $ vim ./mysite/blog/template/base.html
{% load static %} 
<!DOCTYPE html>
<html>
    <head>
    ...
    <link rel="icon"href="{% static 'favicon.ico' %}">
    </head>
    <body>
    ...
    </body>
</html>


# Использование канонических URL-адресов для моделей
====================================================
http://127.0.0.1:8000/blog/

# В целях формирования URL-адресов будем использовать дату публикации publish и значения slug.

    $ python ./mysite/manage.py makemigrations blog
Migrations for 'blog':
mysite/blog/migrations/0002_alter_post_slug.py
  - Alter field slug on post
    $ python ./mysite/manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0002_alter_post_slug... OK
# Django только что создал файл 0002_alter_post_slug.py внутри каталога migrations приложения blog и применил существуюшие миграции.


# Добавление постраничной разбивки в представление списка постов
================================================================
[стр.87]
    $ vim ./mysite/blog/views.py
    $ vim ./230619-django2/mysite/blog/templates/pagination.html
По URL-адресу http://127.0.0.1:8000/admin/blog/post/ создаем в общей
сложности четыре разных новых поста.

# Обработка ошибок постраничной разбивки
[стр.91]
    $ vim ./mysite/blog/views.py
    

# Разработка представлений на основе классов
============================================
[стр.95]
    $ vim ./mysite/blog/views.py