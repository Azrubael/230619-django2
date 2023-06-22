2023-06-21  16:23
=================


    $ source my_env/bin/activate
    $ python ./mysite/manage.py shell
Python 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> Post.Status.choices
[('DF', 'DRAFT'), ('PB', 'Published')]
>>> Post.Status.labels
['DRAFT', 'Published']
>>> Post.Status.values
['DF', 'PB']
>>> Post.Status.names
['DRAFT', 'PUBLUSHED']
>>>


# Добавление взаимосвязи многие-к-одному
========================================
Встроенный в Django фреймворк аутентификации располагается в пакете django.contrib.auth и содержит модель User
Прежде всего необходимо создать первоначальную миграцию модели Post следующей командой из корневого каталога проекта:
    $ python manage.py makemigrations blog
    $ python ./mysite/manage.py makemigrations blog
Migrations for 'blog':
  mysite/blog/migrations/0001_initial.py
    - Create model Post
    - Create index blog_post_publish_bb7600_idx on field(s) -publish of model post

# Внутри каталога миграций приложения blog Django создал файл ./mysite/blog/migrations/0001_initial.py. Эта миграция содержит инструкции SQL по созданию таблицы базы данных для модели Post и определения индекса базы данных для поля publish.

    $ python ./mysite/manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "status" varchar(2) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create index blog_post_publish_bb7600_idx on field(s) -publish of model post
--
CREATE INDEX "blog_post_publish_bb7600_idx" ON "blog_post" ("publish" DESC);
CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;

    $ python ./mysite/manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK

# Мы только что применили миграции приложений, перечисленных в IN-STALLED_APPS, включая приложение blog.
# Если вы внесете в файл models.py любые правки, то вам придется создать новые миграции, снова применив команду makemigrations (дать возможность Django отслеживать изменения модели).
# Затем следует применить миграцию командой migrate, чтобы синхро низировать базу данных с моделями.


# Создание сайта администрирования для моделей
==============================================
# Django идет в комплекте со встроенным интерфейсом администрирова ния, который широко используется для редактирования контента.
# Сперва необходимо создать пользователя, который будет иметь право управлять сайтом администрирования
    $ python manage.py createsuperuser
# Запуск сервера разработки
    $ python ./mysite/manage.py runserver
# https://localhost:8000    
  
    
# Работа с наборами запросов QuerySet и менеджерами
===================================================
    $ python ./mysite/manage.py shell
>>> from blog.models import Post
>>> from blog.models import User
>>> user = User.objects.get(username='adm')
>>> post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
>>> post.save()
# Приведенное выше действие за кулисами выполняет инструкцию SQL INSERT
# Создавать объект и сохранять его в базе данных также можно одной операцией, используя метод create():
>>> Post.objects.create(title='One more post', slug='one-more-post', body='Post body.', author=user)
<Post: One more post>
# Проверяем появление новых постов: http://localhost:8000/admin/blog/post/
# Затем обновим заголовок 'Another post' на 'New title'

>>> post.title = 'New title'
>>> post.save()
# На этот раз метод save() исполняет инструкцию SQL UPDATE


# Извлечение и удавление объектов
=================================
>>> Post.objects.all()
<QuerySet [<Post: One more post>, <Post: New title>, <Post: Who was Django Reinhardt???>, <Post: Who was Django Reinhardt?>]>

>>> Post.objects.filter(publish__year=2023, author__username='admin')
# Это приравнивается к формированию одного и того же набора запросов QuerySet, соединяющего несколько фильтров в цепочку:
>>> Post.objects.filter(publish__year=2023) \
>>>         .filter(author__username='admin')       <- двойная фильтрация
>>> Post.objects.filter(publish__year=2023) \
>>>         .exclude(title__startswith='Why')       <- фильтрация + исключение
>>> post = Post.objects.get(id=1)
>>> post.delete()


# Создание модельных менеджеров
===============================
стр.65