import math


class Area:
    counter = 0

    @staticmethod
    def heron(a, b, c):
        s = (a + b + c) / 2
        Area.counter += 1
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)

    @staticmethod
    def triangle(a, h):
        Area.counter += 1
        return h * a / 2

    @staticmethod
    def square(a):
        Area.counter += 1
        return a ** 2

    @staticmethod
    def rectangle(a, b):
        Area.counter += 1
        return a * b

    @staticmethod
    def calc_counter():
        return Area.counter


print("Площадь треугольника по формуле Герона: ", Area.heron(3, 4, 5))
print("Площадь треугольника через основание и высоту: ", Area.triangle(6, 7))
print("Площадь квадрата: ", Area.square(7))
print("Площадь прямоугольника: ", Area.rectangle(2, 6))

# Вызов счетчика для получения текущего значения
print("Количество вызовов методов: ", Area.calc_counter())
