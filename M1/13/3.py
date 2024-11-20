import json
import pickle

# Создание Python-объекта (словаря)
data = [{'name': 'Alice', 'age': 30, 'city': 'New York'} for _ in range(100)]
# Сериализация в JSON
json_string = json.dumps(data)
print(json_string)
# Вывод: {"name": "Alice", "age": 30, "city": "New York"}

# Запись в файл
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

# Запись в файл
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Чтение из файла
with open('data.json', 'r') as f:
    data_from_file = json.load(f)
    print(data_from_file)
# Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Десериализация строки JSON
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)
print(data)  # Вывод: {'name': 'Bob', 'age': 25}
