import datetime
import threading

# Создание объекта ThreadLocal
local_data = threading.local()


def process_data():
    # Присвоение значения локальной переменной потока
    local_data.value = datetime.datetime.now()
    # Доступ к локальной переменной потока
    print(f'Value in {threading.current_thread().name} : {local_data.value}')


for i in range(50):
    t = threading.Thread(target=process_data)
    t.start()
