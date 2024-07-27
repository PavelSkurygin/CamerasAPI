# CamerasAPI
Тестовое задание на позицию Backend-разработчик на языке Python.

Разработана модель при помощи фреймворка Django со следующими полями первых 10 объявлениях по ссылке:
    https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/
    
Поля БД:
--заголовок объявления;
--id объявления;
--автор объявления;
--количество просмотров объявления;
--позиция, на которой стоит объявление.
Данные добавлены в БД вручную.

Разработаны методы API для обращения к данным моделям. 
Запрос к API имеет параметр ID. При обращении, API возвращает информации об объявлении с ID, переданным в запросе, в формате JSON.

Дополнительные требования:
Реализована система регистрации и входа (верификации аккаунта) для подключения к API (без функционала смены и/или восстановления пароля);
Все обращения к базе данных реализованы при помощи ORM запросов.
