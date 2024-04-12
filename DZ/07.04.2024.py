class Car:

    def __init__(self, marca, year, factory, power, color, price):
        self.marca = marca
        self.year = year
        self.factory = factory
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.marca}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.factory}")
        print(f"Мощность двигателя: {self.power}")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
        print("=" * 40)

    def set_marca(self, marca):  # устанавливаем новое имя
        self.marca = marca

    def get_marca(self):  # получаем имя
        return self.marca

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_factory(self, factory):
        self.factory = factory

    def get_factory(self):
        return self.factory

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


h1 = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10 790 000")
h1.print_info()
h1.set_marca("X5")
print(h1.get_marca())
h1.set_year("2024")
print(h1.get_year())
h1.set_factory("AUDI")
print(h1.get_factory())
h1.set_power("600 л.с.")
print(h1.get_power())
h1.set_color("red")
print(h1.get_color())
h1.set_price("12 000 000")
print(h1.get_price())
