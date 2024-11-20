import pickle

data = {'name': 'Alice', 'age': 30}
# Сохраняем словарь в файл

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Загружаем словарь из файла
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

loaded_data['new'] = 'data'
print(loaded_data)  # Вывод: {'name': 'Alice', 'age': 30}
