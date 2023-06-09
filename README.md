# Тестовое задание для _Python_-программиста. Задача 1
# Веб-сервис "Quiz of questions task 1"

## Веб-сервис выполняет следующие функции:
  
  1. В сервисе реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.
  2. После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
  3. Далее, полученные ответы сохраняются в базе данных: ID вопроса, текст вопроса, текст ответа,  дата создания вопроса, дата изменения вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняются дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
  4. Ответом на запрос из п.2.a будет предыдущий сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

  ### Stack
  [![Flask][Flask]][Flask-url] [![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url] [![PostgreSQL][PostgreSQL]][PostgreSQL-url] [![Docker][Docker]][Docker-url]


## Инструкция по сборке и запуску сервиса
  
  1. Предполагается, что у пользователя уже установлены docker и docker-compose
  
  2. Клонируйте репозиторий
     ```sh
     git clone https://github.com/KonstantinMoseyko/quiz_of_questions_task_1.git
     ```
  
  3. Скопируйте и переименуйте .env.template в .env
     ```sh
     cp .env.template .env
     ```
  
  4. С помощью docker-compose билдим и апаем контейнеры
     ```sh
     docker compose build
     docker compose up
     ```

  5. Далее с помощью curl или другого инструмента делаем POST-запрос на http://127.0.0.1:5000/api/, например:
     ```sh
     curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 3}' http://127.0.0.1:5000/api/
     ```
  
     У сервиса имеется свой GUI, перейдя по ссылке http://127.0.0.1:5000/question/ можно ознакомиться с вопросами которые записаны в БД.



<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Flask]: https://img.shields.io/badge/flask-778876?style=for-the-badge&logo=flask&logoColor=black
[Flask-url]: https://palletsprojects.com/p/flask/
[SQLAlchemy]: https://img.shields.io/badge/sqlalchemy-778876?style=for-the-badge&logo=python&logoColor=black
[SQLAlchemy-url]: https://www.sqlalchemy.org/
[Docker]: https://img.shields.io/badge/Docker-230db7?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-233161?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/