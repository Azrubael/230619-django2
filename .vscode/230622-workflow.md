# 2023-06-22  09:22
===================

# Сохранение проекта Django 4 в репозиторий Git
    $ cd 230619-django2
    $ source my_env/bin/activate
    $ pip install python-decouple
Collecting python-decouple
  Using cached python_decouple-3.8-py3-none-any.whl (9.9 kB)
Installing collected packages: python-decouple
Successfully installed python-decouple-3.8

    $ python -m pip freeze > dependencies.txt
asgiref==3.7.2
Django==4.1.9
python-decouple==3.8
sqlparse==0.4.4
typing_extensions==4.6.3
# What is the difference between django-environ and python-decouple?

    $ git init
    $ git add .
    $ git status
On branch main
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   .gitignore
	new file:   .vscode/230620-workflow.md
	new file:   .vscode/230621-workflow.md
	new file:   .vscode/230622-workflow.md
	new file:   .vscode/dotenv.png
	new file:   .vscode/requirements.png
	new file:   dependencies.txt
	new file:   mysite/blog/__init__.py
	new file:   mysite/blog/admin.py
	new file:   mysite/blog/apps.py
	new file:   mysite/blog/migrations/0001_initial.py
	new file:   mysite/blog/migrations/__init__.py
	new file:   mysite/blog/models.py
	new file:   mysite/blog/tests.py
	new file:   mysite/blog/views.py
	new file:   mysite/db.sqlite3
	new file:   mysite/manage.py
	new file:   mysite/mysite/__init__.py
	new file:   mysite/mysite/asgi.py
	new file:   mysite/mysite/settings.py
	new file:   mysite/mysite/urls.py
	new file:   mysite/mysite/wsgi.py
    $ git commit -m "Step #01. Initial commit. Basic functionality of the first aplication 'blog' of a new project 'mysite'. Authorization and python-decouple dependency."
    
    
    $ python ./mysite/manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 22, 2023 - 06:54:31
Django version 4.1.9, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


# Создание модельных менеджеров
===============================
стр.65
# Реализуем менеджер, который позволит извлекать посты, используя обозначение Post.published.all()
    $ vim ./mysite/blog/models.py
    
# Далее займемся тестированием вновь созданного менеджера
    $ python manage.py shell
>>> from blog.models import Post
>>> Post.published.filter(title__startswith='Who')
<QuerySet []>
>>> exit()


# Разработка представлений списка и детальной информации
    $ vim ./mysite/blog/views.py
    
# Добавление шаблонов URL-адресов представлений    [стр.71]
    $ vim ./mysite/blog/urls.py
# Далее необходимо вставить шаблоны URL-адресов приложения blog в главные шаблоны URL-адресов проекта. Редактируем файл urls.py, расположенный внутри mysite проекта
    $ vim ./mysite/mysite/urls.py
# Именные пространства должны быть уникальными дя всего проекта


# Создание шаблонов представлений
==================================
Внутри каталога приложения blog создаем следующие ниже каталоги и файлы:
templates/
    blog/
    base.html
    post/
        list.html
        detail.html
        
[стр.74]