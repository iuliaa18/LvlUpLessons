# class Name_class:
# Класс – это проект объекта.
# __init__

class Car:
    def __init__(self, brend, model, color, mileage):
        self.brend = brend
        self.model = model
        self.color = color
        self.mileage = mileage

    def print_brend(self):
        print(f"Марка автомобиля: {self.brend}")

    def print_model(self):
        print(f"Модель: {self.model}")

    def print_color(self):
        print(f"Цвет: {self.color}")

    def print_mileage(self):
        print(f"Пробег: {self.mileage} км")

    def run(self):
        s = int(input("Укажите пройденное расстояние в км: "))
        self.mileage += s
        print(f"Пробег {self.mileage} км")

car1 = Car("BMW", "X5", "Чёрный", 79000)
car2 = Car("Nissan", "Skyline IX", "Белый", 200000)

car1.print_brend()
car1.print_model()
car1.print_color()
car1.print_mileage()
car1.run()
car1.run()
car1.run()
car2.print_brend()
car2.print_model()
car2.print_color()
car2.print_mileage()
car2.run()
car2.run()

# Логические методы:
# __str__ преобразование в строку , __add__ , __sub__, __mul__, __int__
# @staticmethod


