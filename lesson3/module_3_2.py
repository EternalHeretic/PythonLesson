def send_email(message:str, recipient:str, * , sender = "university.help@gmail.com"):
    pattern = '@'
    pattern_domen_com   = '.com'
    pattern_domen_ru    = '.ru'
    pattern_domen_net   = '.net'

    if not all ([   pattern in recipient,
                    pattern in sender,
                    recipient.endswith(pattern_domen_ru) or
                    recipient.endswith(pattern_domen_net) or
                    recipient.endswith(pattern_domen_com),
                    sender.endswith(pattern_domen_ru) or
                    sender.endswith(pattern_domen_net) or
                    sender.endswith(pattern_domen_com)
                ]):
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

    elif recipient == sender:
        print(f"Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.ru')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')