
class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):  # проверку здесь сделать в сеттере
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        print(f"Прямоугольник {self.color}, Площадь: ", end="")
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w <= 0:
            raise TypeError("Число должно быть положительным")
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h <= 0:
            raise TypeError("Число должно быть положительным")
        self.__height = h


rect = Rectangle(10, 20, "green")
print(rect.area())
