import smtplib

mailtext = """\
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

name1 = "%friend_name%" #Имя получателя
name2 =  "%my_name%" #Имя отправителя
site_name = "%website%" #Ссылка на сайт

address_from = "denis222mail@yandex.ru" #Адрес отправителя
address_to = "tyrischev.d.v@yandex.ru" #Адрес получателя
subject_mail = "Приглашение!" #Заголовок письма
content_mail_type = 'text/plain; charset="UTF-8";' #Контент тип

address_name = ('''\
From:{address_from}
To:{address_to}
Subject:{subject_mail}
Content-Type:{content_mail_type}
'''.format(address_from=address_from, address_to=address_to, subject_mail = subject_mail, content_mail_type=content_mail_type)) #Заголовок письма

address_name = address_name.encode("UTF-8")

mailtext = mailtext.replace(name1,"Иван")
mailtext = mailtext.replace(name2,"Денис")
mailtext = mailtext.replace(site_name,"https://dvmn.org/profession-ref-program/tyrischev.d.v/MUaFd/")

print(address_name)
print("")
print(mailtext)

server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
login_ya = ("denis222mail@yandex.ru")
password_ya = ("hdnaiwlblhhjaxlt")
server.login(login_ya, password_ya)
server.sendmail("denis222mail@yandex.ru","tyrischev.d.v@yandex.ru" , "mailtext")
server.quit()