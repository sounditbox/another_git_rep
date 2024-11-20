import poplib
from credentials import username, password
# Учётные данные для входа


# Подключение к почтовому серверу Gmail
pop3_server = 'pop.gmail.com'
mailbox = poplib.POP3_SSL(pop3_server, 995)

# Вход в почтовый ящик
mailbox.user(username)
mailbox.pass_(password)

# Получение информации о почтовом ящике
num_messages = len(mailbox.list()[1])
print(f"Количество писем: {num_messages}")

# Пример: Чтение последнего письма
if num_messages > 0:
    response, lines, octets = mailbox.retr(num_messages)
    message = '\n'.join(line.decode('utf-8') for line in lines)
    print("Содержимое последнего письма:")
    print(message)

# Закрытие соединения
mailbox.quit()
