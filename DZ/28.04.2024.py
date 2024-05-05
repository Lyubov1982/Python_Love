class Cloc:
    __DAY = 86400  # Число секунд в одном дне

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Cloc.__get_form(h)}:{Cloc.__get_form(m)}:{Cloc.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return Cloc(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return Cloc(self.sec - other.sec)

    def __isub__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        self.sec -= other.sec
        return self

    def __mul__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return Cloc(self.sec * other.sec)

    def __imul__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        self.sec *= other.sec
        return self

    def __floordiv__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return Cloc(self.sec // other.sec)

    def __ifloordiv__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        self.sec //= other.sec
        return self

    def __mod__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return Cloc(self.sec % other.sec)

    def __imod__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        self.sec %= other.sec
        return self

    def __eq__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return self.sec < other.sec

    def __le__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return self.sec <= other.sec

    def __gt__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Cloc):
            raise ArithmeticError("Правый операнд должен быть типом данным Clock")
        return self.sec >= other.sec


c1 = Cloc(100)
c2 = Cloc(200)
print(c1.get_format_time())
print(c2.get_format_time())
c3 = c1 + c2
print(c3.get_format_time())
# c4 = c1 + c2 + c3
# print(c4.get_format_time())
# c5 = c3 - c2
# print(c5.get_format_time())
c6 = c1 * c2
print(c6.get_format_time())
c7 = c1 // c2
print(c7.get_format_time())
c8 = c1 % c2
print(c8.get_format_time())
c1 -= c2
c9 = c1
print(c9.get_format_time())
c1 *= c2
c10 = c1
print(c10.get_format_time())
c1 //= c2
c11 = c1
print(c11.get_format_time())
c1 %= c2
c12 = c1
print(c12.get_format_time())

# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время равно")

if c3 < c1:
    print("True")
else:
    print("False")

if c3 <= c1:
    print("True")
else:
    print("False")

if c3 > c1:
    print("True")
else:
    print("False")

if c3 >= c1:
    print("True")
else:
    print("False")
