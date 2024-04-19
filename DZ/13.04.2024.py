class Person:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, (int, float)):
            self.__age = new_age
        else:
            print("Возраст задается только числами")

    @age.deleter
    def age(self):
        del self.__age

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name


one = Person("Irina", 26)
print(one.name, one.age)
one.name = "Igor"
one.age = 31
print(one.name, one.age)
