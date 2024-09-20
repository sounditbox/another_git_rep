import socket

# Создаем сокет TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
host = 'localhost'
port = 12345
client_socket.connect((host, port))


# Отправляем данные на сервер
while True:

    message = input('write "exit" for exit:\n')
    if message == 'exit':
        client_socket.sendall(message.encode())
        break
    client_socket.sendall(message.encode())

    # Получаем ответ от сервера
    data = client_socket.recv(1024).decode()
    print(data)

# Закрываем соединение
client_socket.close()
