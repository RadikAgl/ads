# Проект сервиса обмена товарами

## log:pass

joe@gmail.com:joe
user6@gmail.com:CurrentUser1
user2@gmail.com:CurrentUser2
user3@gmail.com:CurrentUser3
user4@gmail.com:CurrentUser4
user5@gmail.com:CurrentUser5

## Запуск СУБД postrgesql

docker run --name test_db -e POSTGRES_USER=username -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test -p 5432:5432 -d postgres

## Настройка и запуск проекта

Для работы сервиса требуются:

- Python версии не ниже 3.10.
- установленное ПО для контейнеризации - [Docker](https://docs.docker.com/engine/install/).

Настройка переменных окружения

1. Создайте и заполните .env файл. Пример:

```yaml
DATABASE_URL=postgresql://username:password@127.0.0.1:5432/test
```

### Запуск СУБД Postgresql

   ```shell
   docker run --name test_db -e POSTGRES_USER=username -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test -p 5432:5432 -d postgres
   ```


### Установка и активация виртуального окружения

   ```shell
   # Создайте виртуальное окружение myvenv
   python -m venv myvenv
   # Активируйте виртуальное окружение
   # Для Windows
   myvenv/Scripts/activate.bat
   # Для Linux и MacOS
   source myvenv/bin/activate
   # Установите зависимости 
   pip install -r /path/to/requirements.txt
   ```
 ### Применение миграций
   ```shell
   python manage.py migrate
   ```

### Запуск тестов
Для запуска тестов выполните следующую команду из папки ads/:
   ```shell
   python manage.py test
   ```


### Как запустить web-сервер

Запуск сервера производится в активированном локальном окружение из папки `ads/`

   ```shell
   python manage.py runserver
   ```

### Загрузка фикстур Django

Для загрузки всех фикстур Django из каталога 'fixtures' в базу данных проекта используйте следующий скрипт:

```bash
python load_fixtures.py
```

Скрипт автоматически обнаружит и загрузит все файлы JSON в указанном каталоге 'fixtures'. Файлы будут обработаны в алфавитном порядке.