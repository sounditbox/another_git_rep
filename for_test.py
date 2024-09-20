from typing import TypedDict


class Movie(TypedDict):
    name: str
    year: int


movie: Movie = {'name': 'Blade Runner',
                'year': 1982}


# movie['director'] = 'Ridley Scott' Error: invalid key 'director'
# movie['year'] = '1982' Error: invalid value type ("int" expected)

# Аннотация работает вот тут: IDE подсказывает, что упущен правильный ключ
movie2: Movie = {'title': 'Back To The Future',
                 'year': 1985}

# Можно и вот так создавать экземпляры класса
m = Movie(name='Star Wars: Return of the Jedi', year=1983)

# При этом тип экземпляра - всё ещё просто словарь:
print(type(m))  # Выведет <class 'dict'>
