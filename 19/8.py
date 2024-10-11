def simple_hash(s):
    hash_value = 0
    for char in s:
        hash_value += ord(char)  # ord() возвращает числовое значение символа
    return hash_value % 10  # возвращаем остаток от деления на 10


print(simple_hash("apple"))  # Пример хеширования строки "apple"
print(simple_hash("banana"))
print(simple_hash("kiwi"))
print(simple_hash("orange"))
print(simple_hash("carrot"))
print(simple_hash("potato"))
print(simple_hash("tomato"))
print(simple_hash("melon"))
print(simple_hash("watermelon"))
