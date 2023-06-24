# 2023-06-24  19:00
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

    
# Рекомендация постов по электронной почте
==========================================
[стр.97]
    $ vim ./mysite/blog/forms.py
    $ vim ./mysite/mysite/settings.py
[стр.106]

    $ python ./mysite/manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Django mail', 'This e-mail was sent with Django.',\
>>> 'peregarien@gmail.com', ['i0638464000@gmail.com'], fail_silently=False)