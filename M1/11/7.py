def add_item(item, items=None):
    """Добавляет элемент в список."""
    if items is not None:
        items.append(item)
    else:
        items = []
    return items


# Первый вызов
print(add_item("apple"))  # Выведет: ['apple']
# Второй вызов
print(add_item("banana"))  # Выведет: ['apple', 'banana']
# Третий вызов
print(add_item("cherry"))  # Выведет: ['apple', 'banana', 'cherry']
