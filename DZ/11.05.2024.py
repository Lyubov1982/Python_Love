class Descriptor:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if self.__name in ('price', 'quantity'):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"{self.__name} должно быть положительным числом")
        instance.__dict__[self.__name] = value


class Order:
    product_name = Descriptor()
    price = Descriptor()
    quantity = Descriptor()

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity


p = Order("apple", 5, 10)
print(p.calculate_price())
