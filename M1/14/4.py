import datetime
import socket

messages = []


# Создаем сокет TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
host = 'localhost'
port = 12345
server_socket.bind((host, port))

# Начинаем прослушивание
server_socket.listen()
print(f"Сервер слушает на {host}:{port}")

# Принимаем соединение
client_socket, addr = server_socket.accept()
print(f"Подключение от {addr}")
while True:
    # Получаем данные от клиента
    mes = client_socket.recv(1024).decode()
    if mes == 'exit':
        break
    messages.append(f'{mes} - {datetime.datetime.now().strftime('%H:%M:%S %d.%m')}')
    # Отправляем ответ
    client_socket.sendall('\n'.join(messages).encode())

# Закрываем соединение
client_socket.close()
