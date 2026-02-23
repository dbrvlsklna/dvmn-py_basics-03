import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('SENDER_EMAIL')
recipient_email = os.getenv('RECIPIENT_EMAIL')
password = os.getenv('APP_PASSWORD')
website = os.getenv('REF_URL')
subject = 'Приглашение!'
email_content_type = 'text/plain; charset="UTF-8"'
recipient_name = 'Петя!'
sender_name = 'Вася'
email_text = f'''From: {sender_email}
To: {recipient_email}
Subject: {subject}
Content-Type: {email_content_type}

Привет, {recipient_name} {sender_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website} 
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''
email_text = email_text.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(sender_email, password)
server.sendmail(sender_email, recipient_email, email_text)
server.quit()

