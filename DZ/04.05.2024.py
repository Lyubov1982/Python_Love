from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name, color):
        self.color = color
        self.name = name

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        print(f"цвет: {self.color} \nпериметр: {self.perimeter()} \nплощадь: {self.area()}")


class Square(Shape):
    def __init__(self, name, a, color):
        super().__init__(name, color)
        self.a = a

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2

    def draw(self):
        for _ in range(self.a):
            print("*" * self.a)

    def info(self):
        print("=" * 3, self.name, "=" * 3)
        print(f"сторона: {self.a}")
        super().info()


class Rectangle(Shape):
    def __init__(self, name, width, height, color):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def draw(self):
        for _ in range(self.width):
            print("*" * self.height)

    def info(self):
        print("=" * 3, self.name, "=" * 3)
        print(f"длина: {self.width} \nширина: {self.height}")
        super().info()


class Triangle(Shape):
    def __init__(self, name, c1, c2, c3, color):
        super().__init__(name, color)
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def perimeter(self):
        return self.c1 + self.c2 + self.c3

    def area(self):
        p = self.perimeter() / 2
        return round((p * (p - self.c1) * (p - self.c2) * (
                p - self.c3)) ** 0.5, 2)

    def draw(self):
        for i in range(self.c2):
            print(" " * (self.c2 - i - 1) + "*" * (2 * i + 1))

    def info(self):
        print("=" * 3, self.name, "=" * 3)
        print(f"сторона 1: {self.c1} \nсторона 2: {self.c2} \nсторона 3: {self.c3}")
        super().info()


s1 = Square("Квадрат", 3, "red")
r1 = Rectangle("Прямоугольник", 3, 7, "green")
t1 = Triangle("Треугольник", 11, 6, 6, "yellow")

shape = [s1, r1, t1]

for g in shape:
    g.info()
    g.draw()
    print()
