# FirstBlog

## Первый Django блог
### Start
#### Локально, сервер разработчика

<code>python manage.py runserver</code>

#### Адреса:

http://localhost:8000/blog1/ - главная

http://localhost:8000/blog1/search/ - поиск постов

#### Посты создаются через admin-пользователя:

<code>python manage.py createsuperuser</code>

#### Cайт администрирования:

http://localhost:8000/admin/blog1/

#### Необходимо создать .py файл с данными для подключения к БД и использования SMTP (В данном проекте использовался mail.ru).

Смотри data_dict_example.py.
