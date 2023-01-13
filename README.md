# FastAPI practice

Backend API для социальной сети.

## Для просмотра проекта:

Клонировать репозиторий и перейти в папку с проектом
```
git clone https://github.com/spltxt/fastapi_practice.git

cd fastapi_practice
```
(Опционально) Создать и активировать виртуальное окружение
```
python -m venv venv

venv\Scripts\activate
```
Установить зависимости
```
pip install -r requirements.txt
```
Запустить локальный сервер
```
uvicorn main:app --reload
```
Перейти в SwaggerUI
```
http://127.0.0.1:8000/docs
```
<b>Функционал:</b>

- Аутентификация: создание пользователя, хэширование пароля, получение токена, авторизация.
- Создание, удаление и редактирование постов.
- Возможность лайкать посты.
- Создание и удаление комментариев.

Пример ответа на запрос о получении всех публикаций:
```
[
  {
    "id": 0,
    "image_url": "string",
    "image_url_type": "string",
    "caption": "string",
    "timestamp": "2023-01-13T01:36:50.006Z",
    "user": {
      "username": "string"
    },
    "comments": [
      {
        "text": "string",
        "username": "string",
        "timestamp": "2023-01-13T01:36:50.006Z"
      }
    ],
    "likes": [
      {
        "username": "string"
      }
    ]
  }
]
```
