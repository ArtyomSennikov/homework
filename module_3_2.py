def send_email (message, recipient, *, sender="university.help@gmail.com"):
    def mail_check ():
        a = ['@']
        b = ['.com', '.ru', '.net']
        result = False
        for i in b:
            if a and i in sender:
                result = True
        return result
    if recipient == sender:
        print("Невозможно отправить письмо самому себе!")
    elif mail_check() == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'Vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')