class Human:
    def __init__(self, name, age):  # Конструктор
        self.name = name
        self.age = age

    def info(self):
        print(f'My name is {self.name} and my age is {self.age}')


a = Human('Andrew', 33)
# a = Human.__init__(a, 'Andrew', 33)
a.info()

b = Human('Bob', 28)
b.info()

