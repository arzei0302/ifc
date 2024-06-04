# FastAPI Project

## Установка и запуск с использованием Docker

### Шаги

1. Установите Docker и Docker Compose:

   - [Инструкции по установке Docker](https://docs.docker.com/get-docker/)
   - [Инструкции по установке Docker Compose](https://docs.docker.com/compose/install/)

2. Клонируйте репозиторий:

   ```sh
   git clone https://github.com/username/repository.git
   cd repository

3. Постройте и запустите контейнеры:

   docker-compose up --build
   docker-compose up 

4. docker-compose down - Эта команда остановит и удалит все контейнеры, сети и тома, созданные Docker Compose для вашего проекта.
   docker-compose stop - Если вы хотите только остановить контейнеры, но оставить их существующими (чтобы запустить их снова без пересоздания).
   docker-compose start - Для повторного запуска остановленных контейнеров.



Приложение будет доступно по адресу http://localhost:8000.

Проверка работы API
Откройте Swagger UI: http://localhost:8000/docs
Откройте ReDoc: http://localhost:8000/redoc

Создание новости (POST):
curl -X POST "http://localhost:8000/ifcnews/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "title=Sample News Title" -F "text=This is the content of the news." -F "image=@/path/to/local/sample_image.jpg" -F "video=@/path/to/local/sample_video.mp4"

Получение списка новостей (GET):
curl -X GET "http://localhost:8000/ifcnews/" -H "accept: application/json"

Получение одной новости по ID (GET):
curl -X GET "http://localhost:8000/ifcnews/1" -H "accept: application/json"

Обновление новости (PUT):
curl -X PUT "http://localhost:8000/ifcnews/1" -H "accept: application/json" -H "Content-Type: application/json" -d '{
  "title": "Updated News Title",
  "text": "This is the updated content of the news.",
  "image": "updated_image.jpg",
  "video": "updated_video.mp4"
}'

Удаление новости (DELETE)
curl -X DELETE "http://localhost:8000/ifcnews/1" -H "accept: application/json"


Компиляция файлов .po в .mo:
msgfmt locale/ru/LC_MESSAGES/messages.po -o locale/ru/LC_MESSAGES/messages.mo
msgfmt locale/en/LC_MESSAGES/messages.po -o locale/en/LC_MESSAGES/messages.mo
msgfmt locale/kg/LC_MESSAGES/messages.po -o locale/kg/LC_MESSAGES/messages.mo


curl -H "Accept-Language: ru" http://127.0.0.1:8000
curl -H "Accept-Language: ru-RU" http://127.0.0.1:8000

curl -H "Accept-Language: en" http://127.0.0.1:8000
curl -H "Accept-Language: kg" http://127.0.0.1:8000



