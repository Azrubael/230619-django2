# 2023-06-22  09:22
===================

# Сохранение проекта Django 4 в репозиторий Git
    $ cd 230619-django2
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

    $ 