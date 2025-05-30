# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможетего запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД. 

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Переменные окружения программы включают:
```
DB_ENGINE — определяет тип используемой базы данных.
DB_HOST — указывает хост, на котором расположена база данных.
DB_PORT — задаёт порт, через который происходит подключение к базе данных.
DB_NAME — имя базы данных, к которой нужно подключиться.
DB_USER — учётная запись пользователя для подключения к базе данных.
DB_PASSWORD — пароль для учётной записи пользователя базы данных.
SECRET_KEY — секретный ключ, используемый для обеспечения безопасности приложения.
```
Эти переменные используются для настройки подключения к базе данных и обеспечения безопасности работы приложения.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).    