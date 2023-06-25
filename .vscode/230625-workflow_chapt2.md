# 2023-06-25  15:57
===================

# Активация виртуальной среды
    $ source my_env/bin/activate
# Запуск сервера разработки
(my_env)$ python ./mysite/manage.py runserver

    
# Отправка электронных писем с помощью Django
=============================================
[стр.106]

    $ python ./mysite/manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Django mail', 'This e-mail was sent with Django.',\
>>> 'peregarien@gmail.com', ['i0638464000@gmail.com'], fail_silently=False)

# Отправка электронных писем в представлениях
=============================================
    $ vim ./mysite/blog/views.py
    $ vim ./mysite/blog/urls.py
    $ vim ./mysite/blog/templates/blog/post/share.py
    $ vim ./mysite/blog/templates/blog/post/detail.py
    
#   http://127.0.0.1:8000/blog/
# Под телом поста должна появиться ссылка, которую только что добавили
# Стили CSS формы email находятся в файле static/css/blog.css


# Создание системы комментариев
===============================
    $ vim ./mysite/blog/models.py
...
class Comment(models.Model):
...

# Разработанная модель Comment не синхронизирована с базой данных, и поэтому необходимо сгенерировать новую миграцию в базе данных, чтобы
# создать соответствующую таблицу базы данных.
    $ python ./mysite/manage.py makemigrations blog
Migrations for 'blog':
  mysite/blog/migrations/0003_comment_comment_blog_commen_created_0e6ed4_idx.py
  - Create model Comment
  - Create index blog_commen_created_0e6ed4_idx on field(s) created of model comment

    $ python ./mysite/manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0003_comment_comment_blog_commen_created_0e6ed4_idx... OK
# Миграция была применена, и в базе данных была создана таблица blog_comment.

# Добавим новую модель на сайт администрирования, чтобы управлять комментариями через простой интерфейс.
    $ vim ./mysite/blog/admin.py
    $ python ./mysite/manage.py runserver
    
# Скомпонуем форму, позволяющую пользователям комментировать посты блога
    $ vim ./mysite/blog/forms.py
    
# Добавим новое обрабатывающее форму представление, которое позволит пользователю возвращаться к представлению детальной информации о посте, после того как комментарий будет сохранен в базе данных.
    $ vim ./mysite/blog/views.py
    $ vim ./mysite/blog/urls.py
    $ vim ./mysite/blog/post/includes/comment_form.html
    $ vim ./mysite/blog/post/comment.html    