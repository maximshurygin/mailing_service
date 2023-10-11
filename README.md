# Описание
Этот Django-проект предназначен для создания и отправки рассылок по электронной почте с различной периодичности. 
Сервис позволяет настроить рассылку, выбрать получателей, задать время и периодичность отправки сообщений.
Для создания рассылки сначала нужно добавить сообщение, клиентов. Затем в окне создания рассылки нужно выбрать сообщение
и клиентов, которые получат сообщение. Так же нужно выбрать время и периодичность рассылки и ее статус.
Статус 'Создана' предназначен для рассылок, которые пользователь сделал, но ему не нужно в данный момент запускать рассылку.
Статус 'Запущена' используется для того, чтобы начать отправку сообщения в соответствии с настройками.
Для того, чтобы завершить рассылку, пользователю необходимо изменить ее статус на 'Завершена'.

# Особенности
- Создание рассылок с выбором получателей и сообщения.
- Возможность установки периодичности рассылок: ежедневно, еженедельно, ежемесячно.
- Возможность установки статуса рассылок: создана, запущена, завершена.
- Автоматическая отправка писем в заданный интервал времени.
- Логирование результатов отправки писем.
- Реализован функционал менеджера.
- Кеширование блога и главной страницы.