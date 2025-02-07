class Car:
    def __init__(self, make, model, year):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.year = year  # Год выпуска
        self.is_started = False  # Флаг, указывающий, заведен ли двигатель

    def start_engine(self):
        self.is_started = True
        print(f"Двигатель {self.make} {self.model} заведен.")

    def stop_engine(self):
        self.is_started = False
        print(f"Двигатель {self.make} {self.model} заглушен.")

    def ride(self, km):
        if self.is_started:
            print(f'Проехали {km} км')
        else:
            print('Двигатель заглушен')


my_car = Car("Ford", "Mustang", 1964)
my_car.start_engine()
my_car.ride(42)
