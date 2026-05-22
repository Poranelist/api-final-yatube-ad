# Yatube API

REST API для социальной платформы Yatube.

Проект позволяет:
- публиковать посты;
- комментировать посты;
- получать список групп;
- подписываться на авторов;
- работать с JWT-аутентификацией.

Документация API (ReDoc): `http://127.0.0.1:8000/redoc/`

## Технологии

- Python 3.9+
- Django 3.2
- Django REST Framework
- SimpleJWT
- Pytest

## Быстрый старт

Клонируйте репозиторий и перейдите в папку проекта:

```powershell
git clone <URL_ВАШЕГО_РЕПО>
Set-Location api-final-yatube-ad
```

Создайте и активируйте виртуальное окружение:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Установите зависимости:

```powershell
pip install -r requirements.txt
```

Перейдите в папку Django-проекта, выполните миграции и запустите сервер:

```powershell
Set-Location .\yatube_api
python manage.py migrate
python manage.py runserver
```

## Аутентификация (JWT)

Получить токен:

```powershell
curl -X POST http://127.0.0.1:8000/api/v1/jwt/create/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"<username>\",\"password\":\"<password>\"}"
```

Обновить токен:

```powershell
curl -X POST http://127.0.0.1:8000/api/v1/jwt/refresh/ ^
  -H "Content-Type: application/json" ^
  -d "{\"refresh\":\"<refresh_token>\"}"
```

## Примеры запросов

Получить посты:

```powershell
curl http://127.0.0.1:8000/api/v1/posts/
```

Создать подписку:

```powershell
curl -X POST http://127.0.0.1:8000/api/v1/follow/ ^
  -H "Authorization: Bearer <access_token>" ^
  -H "Content-Type: application/json" ^
  -d "{\"following\":\"<username>\"}"
```

Получить свои подписки:

```powershell
curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:8000/api/v1/follow/
```

## Структура проекта

- `yatube_api/` - Django-проект
- `yatube_api/api/` - API-приложение (viewsets, serializers, urls)
- `yatube_api/posts/` - модели постов, комментариев, подписок
- `tests/` - автотесты
- `postman_collection/` - Postman-коллекция
