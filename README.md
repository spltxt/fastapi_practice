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
- Создание и удаление постов.
- Загрузка изображений.
- Создание и удаление комментариев.

Пример ответа на запрос о получении всех публикаций:
```
[
  {
    "id": 1,
    "image_url": "string",
    "image_url_type": "absolute",
    "caption": "test_caption",
    "timestamp": "2022-12-12T16:57:09.193Z",
    "user": {
      "username": "testUser"
    },
    "comments": [
      {
        "text": "test comment",
        "username": "testUser",
        "timestamp": "2022-12-12T16:57:20.193Z"
      }
    ]
  }
]
```
