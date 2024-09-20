file = open('in.txt', encoding='utf-8')
# Возвращает номер байта, где находится "курсор"
part = file.read(5)
print(part)
print(file.tell())
file.seek(11)  # Сдвигает "курсор" на n-ый байт.
part = file.read(5)
print(part)
file.close()

