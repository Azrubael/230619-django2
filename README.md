[1] - Install Python 3.10 (or later), pip и python3.10-venv
* https://docs.python.org/3/using/windows.html#launcher
* https://pip.pypa.io/en/stable/installing/
```bash
    apt install python3.10-venv
```


[2] - Create isolated invironment
* For Linux
```bash
    $ python3 -m venv my_env
    $ source my_env/bin/activate
```
* For Windows
```bash
    $ py -m venv my_wenv
    $ .\my_wenv\Scripts\activate
```


[3] - Activate virtual environment:

```bash
    $ source my_env/bin/activate
```


[4] - Restore dependencies:
```bash
(my_env)$ pip install -r dependencies.txt
```


[5] - Start local dev server:
```bash
(my_env)$ python ./mysite/manage.py runserver
```


[6] - Create list of dependencies
```bash
(my_env)$ pip freeze > dependencies.txt
```


[7] - To deactivate isolated environment
```bash
(my_env)$ deactivate
```