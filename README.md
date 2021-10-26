# SERVIS_FASTAPI

Сервис ринимает номер телефона стандартизирует его и отдает обратно.
Обрабатывает запросы в виде JSON, данные формы, query параметры и данные Cookies

Веб-сервис принимает запросы на соотвецтвующие адрес 

POST:   /unify_phone_from_json, 

POST:   /unify_phone_from_form, 

GET:   /unify_phone_from_query, 

GET:   /unify_phone_from_cookies, 

Запуск при помощи команды:

uvicorn main:app --reload
