import math
from math import pi

form = int(input("Вычисление площади фигур\n\n1 - треугольник\n2 - прямоугольник\n3 - круг\nВыберите фигуру: "))

if form == 1:
    side_a = int(input("Введите сторону а: "))
    side_b = int(input("Введите сторону b: "))
    side_c = int(input("Введите сторону c: "))
    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    area_r = round(area, 2)
    print("Площадь треугольника:", area_r)

elif form == 2:
    length_a = int(input("Введите длину стороны а: "))
    length_b = int(input("Введите длину стороны b: "))
    square = length_a * length_b
    print("Площадь прямоугольника:", square)

elif form == 3:
    radius = int(input("Введите радиус окружности: "))
    print("Длина окружности: ", round(2 * pi * radius, 2))
else:
    print("Неверный выбор фигуры.")
