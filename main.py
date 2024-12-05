import os
from dotenv import load_dotenv
load_dotenv()
import smtplib

TOKEN = os.getenv("TOKEN")
LOGIN = os.getenv("LOGIN")

mailtext = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""" #Шаблон письма

friend_name = "%friend_name%"
my_name =  "%my_name%"
site_name = "%website%"

address_from = "tyrischev.d.v@gmail.com"
address_to = "tyrischev.d.v@yandex.ru"
subject_mail = "Приглашение!"
content_mail_type = 'text/plain; charset="UTF-8";'

mailtext = mailtext.replace(friend_name,"Иван")
mailtext = mailtext.replace(my_name,"Денис")
mailtext = mailtext.replace(site_name,"https://dvmn.org/profession-ref-program/tyrischev.d.v/MUaFd/")

address_name = ('''\
From:{address_from}
To:{address_to}
Subject:{subject_mail}
Content-Type:{content_mail_type}

{mailtext}
'''.format(address_from=address_from, address_to=address_to, subject_mail = subject_mail, content_mail_type=content_mail_type, mailtext=mailtext)) #Заголовок письма
address_name = address_name.encode("UTF-8")

server = smtplib.SMTP_SSL("smtp.gmail.com:465")
server.ehlo()
server.login(LOGIN, TOKEN)
server.sendmail("address_from", "tyrischev.d.v@yandex.ru" , address_name)
server.quit()