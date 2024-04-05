# name = "Nikolay"
# print("Hello," + name + "!")
# a = 30
# b = "Hello"
# c = 2.8
# print(type(a))
# print(type(c))
# print(type(b))
# a = 5
# print(a, type(a))
# b = "Hello"
# print(b, type(b))
# print(str(a) + b)

# a = 5
# print(a, id(a))
# b = 4
# print(b, id(b))
# a = b
# print(a, id(a))

# a = 5
# b = 4
# a = b = c = 4
# print(id(a), id(b), id(c))

# a, b, c, = 5, "Hello", 9.2
# print(a, b, c)

# PI = 3.14  # если переменная в верхнем регистре, такой элемент изменять не нужно (соглашение программистов)
# print(PI)
# PI = 2
# print(PI)

# a = 21 # Домашняя работа!!!!!
# b = 512
# print("a:", a)
# print("b:", b)
# a, b = b, a
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# print("a:", a)
# print("b:", b)

# print("строка символов строка символов строка"
#       "символов строка символов волов строка символов"
#       "строка символов строка символов")
# print('строка \n символов')
#
# print('Документ \"file.txt\" \n находится по пути \rD: \\folder\\file.txt')
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!"
# print(s1 + ", " + s2 + "!")
# print(s3 * 5)

# print(656464646494646464666)
# print(6.56464646494646464666)

# print(60 + 2)
# print(60 - 2)
# print(60 * 2)
# print(6 / 2)  # 3
# print(6 / 4)  # 1.5
#
# print(6 // 2)  # 3
# print(6 // 4)  # 1
#
# print(6 ** 3)  # 2.55 домашка
# print(6 % 4)

# 20/01/2024 python lesson2
# number = (6 + 4) * (5 ** 2+7)  # скобки, степень, умножение, сложение, слева на право
# print(number)

# num = 10
# num += 5  # num = num + 5 = 15
# print(num)
#
# num -= 3  # num = num - 3 = 12
# print(num)

# задача
# num = 4321  # 43
# print(num)
# a = num % 10
# print("a:", a)
# num = num // 10#
# print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# print(num)
# d = num % 10
# print("d:", d)
# print(a * 1000 + b * 100 + c * 10 + d)
# num = 4321
# print(num)
# res = num % 10 * 1000  # 1000
# num //= 10  # num = num //10
# res += num % 10 * 100  # 200
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = "2.5"
# num2 = 3
# # res = num1 + str(num2)  # 23
# # print(res)
# res = float(num1) + num2  # 5
# print(res)

# print(int(2.5))  # 2
# print(round(2.51))  # 3
# print(round(2.519, 2))  # 2.59
#
# a = 2.519
# b = round(a)
# print(b, type(b))
# c = round(a, 2)
# print(c, type(c))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне ", age, " лет.", sep="", end="\n\n")
# print("Hello")

# name = input("Введите имя: ")
# print("Hello,", name)

# Задача 1.20 (время лекции)
# num = int(input("Введите число 1: "))
# power = int(input("Введите число 2: "))
# three = int(input("Введите число 3: "))
# four = int(input("Введите число 4: "))
#
# # num = int(num)
# # power = int(power)
# res1 = num + power
# res2 = three + four
# print("Результат:", round(res1 / res2), 2)
# # print("Число", num, "в степени", power, "равно:", res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5 = 6
# print(b2 + 5)  # 0 + 5 = 5

# print(bool("python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool(4523))
# print(bool(-4))
# print(bool(4.2))
# print(bool(0))  # False
# print(bool(0.0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print(2 > 5)
# print(2 < 5)
# print(2 >= 5)
# print(2 <= 5)
# print("привет" > "ПРИВЕТ")  # 1087 > 1055
# print(ord("П")) 1055
# print(ord("п")) 1087

# print(2 < 4 < 9)  # True && True => True
# print(2 * 5 > 7 >= 4 + 3)  # True 2*5=10 > 7 >=  4+3=7 True; True && True
# print(3 * 3 <= 7 >= 2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True : False => False
# print(5 - 3 > 2 and 1 + 3 == 4)  # False : True => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False : False => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True : False => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False : True => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False : False => False

# print(not 9 - 5)  # False
# print(not 9 - 9)  # True

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")  # pass - закрыть блок (заглушка)
#     # pass
#     ...
# else:
#     print("Доступ запрещен")

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")
#
# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("b == a")

# a = (input("Введите сторону 1: "))
# b = (input("Введите сторону 2: "))
# c = (input("Введите сторону 3: "))
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:  # 6 <=day <= 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")


# mont = int(input("Введите месяц (цифрой): "))
# if 1 <= mont <= 12:  # (day >= 1) and (day <= 5):
#     if mont == 1:
#         print("зима")
#     if mont == 2:
#         print("зима")
#     if mont == 3:
#         print("весна")
#     if mont == 4:
#         print("весна")
#     if mont == 5:
#         print("весна")
#     if mont == 6:
#         print("лето")
#     if mont == 7:
#         print("лето")
#     if mont == 8:
#         print("лето")
#     if mont == 9:
#         print("осень")
#     if mont == 10:
#         print("осень")
#     if mont == 11:
#         print("зима")
#     if mont == 12:
#         print("зима")
# else:
#     print("Такого месяца не существует!")

# month = int(input("Введите номер месяца: "))
# if 3 <= month <= 5:
#     print("Весна")
#     elif 6 <= month <= 8:
#         print("Лето")
#     elif 9 <= month <= 11:
#         print("Осень")
#     elif 1 <= month <= 2 or month == 12:
#         print("Зима")
# else:
#     print("Такого месяца не существует")

# 21/01/2024

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")
#
# password = "admin"
# match password:
#      case "admin":
#          print("Администратор")
#      case "user"
#         print("Пользователь")
#      case _:
#          print("Такого значения не существует")

# day = "четверг"
# time = 17
# match day:
#     case "Понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 20, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b, = 20, 10
# print("на ноль делить нельзя" if b == 0 else a / b)

# a = 5
# b = 0
# print(a / b)

# n = int(input("Введите целое число: "))  # 59 минут все переслушать!!!!
# print(n * 2)

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# # finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)

# Циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Укажите количество символов: "))
# print(n * "+-")  # +-+-+-
# print(n * "+" if n % 2 == 0 else n * "-", end="")
#
# i = 0
# while i < n:
#     print(i * "+" if i % 2 == 0 else i * "-")
#     # if i % 2 == 0:
#     #     print("+", end="")
#     # else:
#     #     print("-", end="")
#     i += 1
#
#
# # while n > 0:
# #     print("*")

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# sum = 0
# while n < m:
#     if n % 2 !=0:
#         sum += n
#     n += 1
#     print(sum)

# n = int(input("Введите начало диапазона: "))
# m = int(input("Введите конец диапазона: "))
# sum_ = 0
# while n <= m:
#     if n % 2: # if n % 2 == 0: четность
#         # print(n, end=" ")
#         sum_ += n
#     n += 1
# print(sum_)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# summ = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     summ *= n
#
# print(summ)

# i = 0
# while i < 10:
#     # if i == 5:
#     # break не дает выполнение else
#     if i == 8:
#         print(5 / 0)  # прерывает полностью
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i=", i)

# 27.01.2023
# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("Внутренний цикл: j=", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j,  end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:  # наружный цикл это строки
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:  # наружный цикл - это строки
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:  # наружный цикл - это строки
#     j = 0
#     while j < 16:  # это столбцы
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
# print()
# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# for element in collection:
#  print(element)

# for i in "Hello!":
#     print(i)
#
# for color in "red", "blue", "green":
#     print(color)
#
# print(range(2, 9, 2))
# range(start, stop, step)
# a = 9
# for i in range(0, a + 1, 1):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 10:
#     print(i, end=" ")
#     i -= 10

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     # if i % 11 == 0:
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# d = [i for i in "Hello"]
# print(d)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список (list)

# nums = [8, 3, 9, 4, "Hello", True]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[2])
# print(nums[-1])
# print(nums[-2])
# nums[1] = 256
# nums[2] += 100
# print(nums)
# # for i in nums:
# #     print(i)
# print(len(nums))

# s = [1, 3, 5]
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))
#
# s2 = s1 + s
# print(s2)
#
# s3 = s * 2
# print(s3)

# n = list(range(10))
# print(n)

# a = [0 for i in range(5)]
# print(a)
#
# a1 = [i ** 2 for i in range(1, 25)]
# print(a1)
#
# a2 = [i * 3 for i in "python"]
# print(a2)

# a = [0] * int(input("Введите количество списков: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# summ = 0
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         summ += a[i]
# for i in a:
#     if i < 0:
#         summ += i
# print(summ)

# s = list(range(10, 100, 10))
# print(s)
# for i in range(len(s)):
#     print(s[i], end=" ")
# print()
# for i in s:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# count = s = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         count += 1
# #     else:
# #         s += n[i]
#
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print("Кол-во четных элементов", count)
# print("Сумма нечетных элементов", s)

# n = list(range(21, 41, 3))
# print(n)
#
# a = 2
# print(n[a])
# print(n[a - 1])

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = count = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         count += 1
# print(s / count)

# a = [7, 9, 2, 1, 17]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез  = список, можем передать в квадратных скобках [start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# print(s[1:3])
# print(s[6:])
# print(s[:])
# print(s[0:5:1])
# print(s[5::-1])
# print(s[0::1])
# print(s[::-1], id(s[::-1]))

# lst = list(range(1, 8))
# print(lst[:])
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[6:])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "Hello"
# print(st)
# print(st[0])
# print(st[0:3])
# print(st[::-1])
#
# a = 54, 56, 57, 58
# print(a[:])
# for i in a:
#     print(i)

# Методы списков dir(list)
# s = [9, 5, 6, 3, 7, 4]
# print(s)
# s.append(8)  # добавили элемент в конец списка (только один элемент)
# print(s)
# s.extend([20, 1, 3])  # добавили элемент в конец списка (несколько элементов)
# s.extend("add")
# print(s)
# s.insert(3, 100)  # добавили элемент по заданному индексу
# s.insert(-1, 222)
# print(s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# s = []
# n = int(input("Введите кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 2 == 0:
#         s.append(x)
#     # s.insert(0, x)
# print(s)

# s = []
# n = int(input("Введите кол-во элементов списка: "))
# for _ in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# # вариант 1
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# # вариант 2
# s = []
# for el in a:
#     if el in b and el not in s:
#         s.append(el)
# print(s)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):  # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)  # [1, 11, 2, 22, 3, 33]

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# a.remove(9)  # удаляет элемент по значению
# # print(a)
# # last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# # print(last)
# # second = a.pop(0)  # удаляет элемент по индексу при указании в рор значения
# # print(second)
# # print(a)
# # a.clear()  # удаляет список
# # print(a)
# num = a.count(9)  # считает кол-во заданных значений в списке
# print(num)
# ind = a.index(9)  # возвращает индекс элемента по заданному значению
# print(ind)
# ind2 = a.index(9, 2)
# print(ind2)

# num = 9
# if num in a:
#     print(a.index(num))

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# a.reverse()
# print(a)

# a = [1, 2, 3]
# b = a.copy()
# print('a =', a)
# print('b =', b)
# a.append(4)
# b.append(120)
# print('a =', a)
# print('b =', b)

# 03/02/2024
# sort сортировка
# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# a.sort()  # сортировка по возрастанию
# a.sort(reverse=True)  # сортировка по убыванию
# print(a)

# s = ["Виталий", "Сергей", "Анна"]
# print(s)
# s.sort()
# print(s)

# sorted сортировка

# генерация случайных данных

# import random

# print(random.random())
# print(random.randint(0, 9))  # 9 включается
# print(random.randrange(3, 9, 2))  # 9 не включается
# print(random.uniform(10.5, 25.5))  # вещественное число, b включается
# print(round(random.uniform(10.5, 25.5), 2))

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# # random.shuffle(s)
# print(s)
# print(random.choice(s))  # выбирает одно случайное значение из списка
# print(random.choices(s, k=3))  # выбирает k= случайное значение из списка

# lst = [input("->") for i in range(10)]  # вводит пользователь
# lst = [random.randint(0, 100) for i in range(10)]  # генерируются цифры сами рандомно
# print(lst)

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# print(len(s))
# print(sum(s))
# print(max(s))
# print(min(s))
#
# s = ["20", "30", "40", "50", "60", "70", "80", "90", "10"]
# print(s)
# print(len(s))
# print(sum(s))  # нельзя суммировать строковые значения
# print(max(s))  # выводит максимальное значение
# print(min(s))  # выводит минимальное значение

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# res = 0
# for i in s:
#     res = res + i
# print(res)
# print(sum(s))  # нельзя суммировать строковые значения

# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# max1 = max(lst)
# print("max: ", max(lst))
# lst.remove(max1)
# lst.insert(0, max1)
# print(lst)

# x = list("1a2b3c4d")
# print(x)
# print("a" in x)
# print("e" in x)
# print("e" not in x)

# s = "c"
# if s in x:
#     print("Такой элемент в списке присутствует")
# else:
#     print(s, "в списке отсутствует")

# lst = []
# # if lst == []:
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# print(bool(lst))

# import random

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("первый список:", a)
# print("второй список:", b)
# c = a + b
# print(c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print(c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)

# n1 = int(input("Размер списка: "))
# # a = [random.randint(0, 10) for i in range(n1)]
# a = []
# while len(a) != n1:
#     n = random.randrange(n1)
#     if n not in a:
#         a.append(n)
# print(a)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1][2])

# s = ["Hello",  "World"]
# print(s[1][0])

# m = [
#     [1, 2, 3, 4, 55],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12, 22, 33]
# ]
# print(m, end="\n\n")
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()

# import random

# w, h = 5, 3
# # matrix = [[random.randint(1, 20) for x in range(w)] for y in range(h)]
# matrix = [[0 for x in range(w)] for y in range(h)]
# # matrix = []
# # for y in range(h):  # 3
# #     new_row = []
# #     for x in range(w):  # 5
# #         new_row.append(0)
# #     matrix.append(new_row)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ") ", x, '+', y, '=', x + y, sep="")

# 04/02/2024
# import math
# num1 = math.sqrt(4)
# num2 = math.pi
# num3 = math.ceil(3.2)  # округляет в большую сторону независимо какой будет остаток
# num4 = math.floor(3.8)  # округляет в меньшую сторону независимо какой будет остаток
# print(num4)
# print(num1)
# print(num2)
# print(num3)

# import math as m
#
# num3 = m.ceil(3.2)  # округляет в большую сторону независимо какой будет остаток
# num4 = m.floor(3.8)  # округляет в меньшую сторону независимо какой будет остаток
# print(num4)
# print(num3)

# from math import *
#
# num3 = ceil(3.2)
# num4 = floor(3.8)
# print(num4)
# print(num3)

# from math import ceil, floor
#
# num3 = ceil(3.2)
# num4 = floor(3.8)
# print(num4)
# print(num3)

# from math import pi
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * radius, 2))

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "")

# second = time.time()
# print(second)
# s = 1523668796
# local_time = time.ctime(s)
# local_time2 = time.ctime()
# print(local_time)
# print(local_time2)
#
# res = time.localtime()
# print(res)
# print("0" + str(res.tm_mday) if res.tm_mday < 10 else res.tm_mday,  ".", res.tm_mon , ".", res.tm_year, sep='')
#
# print(time.strftime("Today is %d/%m/%Y, %H:%M:%S", time.localtime(s)))
#
# print(time.strftime("Сегодня: %B %d, %Y, %A"))

# start = time.monotonic()
# pause = 5
# print("Программа запущена...")
# time.sleep(pause)
# print("Пауза была", pause, "секунд")
# finish = time.monotonic()
# res = finish - start
# print(res)
#
# start = time.time()
# pause = 5
# print("Программа запущена...")
# time.sleep(pause)
# print("Пауза была", pause, "секунд")
# finish = time.time()
# res = finish - start
# print(res)

# Функции ключевое слово def
# print()
#
#
# def hello(name, age):
#     print("Мне", age, "Меня зовут", name)
#
#
# hello("Irina", 28)


# def get_sum(a, b):
#     print("Сумма: ", end='')
#     return a + b
#
#
# n = 2
# m = 5
# # print(get_sum(n, m))
# res = get_sum(n, m)
# print(res)
# print(res + 5 - 2)
# c = 3
# d = 7
# get_sum(c, d)
#
# def maximum(one, two)
#     if one > two:
#         return one
#     else:
#         return two


# print(maximum(9, 6))
# print(maximum(9, 16))


# def count(n, m):
#     if n > m:
#         return n - m
#     else:
#         return n - m
#
#
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# print(count(a, b))

# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()  # удалили последний элемент
#     start = lst.pop(0)  # удалили первый элемент
#     lst.insert(0, end)  # добавляем элементы в начало списка
#     lst.append(start)  # добавили в конец списка элемент
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# print(maximum(9, 6))
# print(maximum(9, 16))
#
# if maximum(9, 16):
#     print("Первое число больше второго")
# else:
#     print("второе число больше первого")

# def check_password(password):
#     has_lower = False
#     has_upper = False
#     has_num = False
#
#     for ch in password:
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_lower and has_upper and has_num:
#         return True
#     else:
#         return False
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль ")
# else:
#     print("Это не надежный пароль")

# 10/02/2024

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s="-"):
#     print(s * c, end="")
#     print()
#
#
# set_param()
# set_param(7)
# set_param(20, "#")
# set_param(15, "+")
# set_param(10, "*")
# set_param(s="#")
# set_param(s="#", c=10)


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:  # even=True
#             s += cur_digit
#         if not even and cur_digit % 2:  # even=False
#             s += cur_digit
#         n //= 10  # n=n//10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")  # работать не будет

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # is - ссылаются ли 2 переменные на один и тот же адрес памяти
# print(id(lt1))
# print(id(lt2))
#
#
#
# a = "Hello"
# b = "Hello"
# print(a == b)  # True
# print(a is b)  # True
# print(id(a))
# print(id(b))
#
# a = a + "_new"
# print(a)
# print(a == b)  # True
# print(a is b)  # True
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(lt1)
# print(id(lt1), id(lt1[0]), id(lt1[1]))
# lt1[1] = 50
# print(lt1)
# print(id(lt1), id(lt1[0]), id(lt1[1]))

# неизменяемые типы данных - int, str, float, bool, tuple
# изменяемый типы данных - lst

# Кортеж (tuple) неизменяемый список

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# print(tpl[0])
# print(type(tpl))

# a = (5,)
# print(a, type(a))

# b = tuple("Hello")
# # b = tuple(["Hello", "World"])
# print(b, type(b))

# a = (5, 9, 7, 3, 4)
# print(a[1:3])
# print(a[-1])
# print(a[4])

# from random import randint
# tpl = tuple(i for i in range(5))
# # tpl = tuple(input("->") for i in range(5))
# # tpl = tuple(randint(1, 100) for i in range(5))   !!!
# tpl = tuple(2 ** i for i in range(1, 13))
# print(tpl)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t3 * 2)
# # print(t3.count("l"))
# # print(t3.index("l", 4, -1))
# sym = 'k'
# # if sym in t3:
# #     print(t3.index(sym, 4, -2))
# # else:
# #     print("Такого символа нет")
#
# try:
#     print(t3.index(sym, 4, -2))
# except ValueError:
#     print("Такого символа нет в заданном диапазоне")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # first = tpl.index(el)
#             # second = tpl.index(el, first + 1) + 1
#             # return tpl[first:second]
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'hi'
# t[4].append('new')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа x, y, z = 1, 2, 3
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()
# # user = get_user()
# # first_name, year, married = user
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(first_name, year, married)

# name = "Igor"
#
# if name:
#     print("Name: ", name)
#     name = "Marina"
#
# print(name)
# name = "Igor"
# for i in range(5):
#     print(i, end=" ")
#     name = "Marina"
#
# print()
# print(name)


# name = "Igor"
#
# def func():
#     print("Hello")
#     # name = "Marina"
#
#
# func()
# print(name)

# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
# print(lst2)
#
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население: ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население: ", city_population, sep="")

# МНОЖЕСТВО (set) - неупорядоченная коллекция (по индексу обратиться не можем), она хранит только уникальные значения

# s = {"red", "green", "blue", "red", "green"}
# print(type(s))
# print(s)
# print(len(s))
#
# for i in s:
#     print(i)

# a = {}  # с пустыми это другой класс dict

# a = set("hello")
# print(a, type(a))
#
# from random import randint
#
# # s = {x * x for x in range(10)}
# # s = {input("->") for x in range(3)}
# s = {randint(20, 50) for x in range(10)}
# print(s)

# s = {"red", "green", "blue"}
# print("green" in s)
# print("green" not in s)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # lt = [i for i in lst if "a" in i]
# # lt = ["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst]
# # lt = ["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"]
# lt = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"}
# print(lt)

# for i in lst:  # 1
#     if i[1] == "c":  # справа только один if
#         if i[0] == "a":  # слева только if, else
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# s = {"red", "green", "blue"}
# print(s)
# s.add("black")  # добавление элемента во множество
# print(s)
# # s.remove("black")  # удаление элемента (KeyError)
# # print(s)
# #
# # color = "pink"
# # if color in s:
# #     s.remove(color)  # (KeyError)
# # print(s)
#
# # s.discard("green")  # удаление элемента по значению не выбрасывая исключения если элемента не существует
# # print(s)
# #
# # color = s.pop()  # удаляет первый элемент из множества
# # print(s)
# # print(color)
#
# s.clear()  # очищает множество
# print(s)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)  # сложение своего рода, без добавления повторяющихся элементов
# c = a | b
# a |= b
# c = a & b # возвращает одинаковые элементы
# a &= b # возвращает одинаковые элементы
# c = a - b # оставляет только уникальный элемент
# a -= b # оставляет только уникальный элемент в переменной a
# c = a ^ b # оставляет уникальные элементы обеих переменных
# a ^= b
# print(a)
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)  # оставляет только одинаковые элементы
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobbies = drawing & music
# print(both_hobbies)
# drawing = drawing - both_hobbies
# print(drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# # a <= b
# # a >= b
# print(a <= b)
# print(a >= b)
# print(a < b)
# print(a > b)
# print(a != b)

# a = [9, 8, 5, 9, 8, 9, 5, 8, 9, 5, 4, 5, 6, 9, 6]
# s = set(a)
# print(a)
# print(s)
# a1 = list(s)
# print(a1)

# # s = frozenset("Hello")
# s = frozenset([9, 8, 5, 6, 7, 4, 2])
# print(s)

# СЛОВАРИ (dict)

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# lst[1] = 200
# d['two'] = 200
# print(lst)
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d, type(d))
#
# d1 = dict(one=1, two=2, three=3)
# print(d1, type(d1))
#
# a = [("a", 1), ("b", 1)]
# d2 = dict(a)
# print(d2)

# ключами могут быть только неизменяемые типы данных и с разными названиями
# d = {0: "text", "one": 45, (1, 2.5): "Кортеж", "список": [2, 3, 6, 5], True: 1, False: 0, 1: "один"}
# print(d)
# d["ne"] = "Новое значение"
# print(d)
#
# # for key in d:
# #     print(key, ":", d[key])
# #
# # key = "one"
# # del d[key]
# # print(d)
#
# key = 45
# try:  # 2 вариант
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + str(key) + " нет в словаре")
#
# # if key in d:  # 1 вариант
# #     del d[key]
# print(d)
# # print("one" in d)
# # print("ne" in d)
#
# # print(d[0])
# # print(d[(1, 2.5)])
# # print(d[False])

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# m = 1
# for key in d:
#     m *= d[key]
# print(m)
#
# d = dict()  # {}
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")

# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.",  sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("Значение не корректно, введите число")
#         else:
#             print("Такого номера не существует")
#     else:
#         break
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.",  sep="")

# d = {"a": 1, "b": 2, "c": 3}
# print(d)
# print(d.keys())  # Только ключи
# print(d.values())  # Только значения
# print(d.items())  # Ключи и значения
#
# for key, value in d.items():
#     print(key, "->", value)
#
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# d = {"a": 1, "b": 2, "c": 3}
# d2 = d.copy()
# print("D = ", d, id(d))
# print("D2 = ", d2, id(d2))
#
# d["b"] = 5
# d2["e"] = 7
# print("D = ", d)
# print("D2 = ", d2)

# d = {"a": 1, "b": 2, "c": 3}
# # print(d["b"])
# # value = d.get("b1", "такого ключа нет")
# # print(value)
# item = d.setdefault("w")  # добавляет несуществующий ключ со значением None
# print(item)
# print(d)

# d = {"a": 1, "b": 2, "c": 3}
# item = d.pop("b", "такого ключа нет")
# print(item)
# print(d)
# item2 = d.popitem()
# print(item2)
# print(d)
# d.clear()
# print(d)

# d = dict.fromkeys(["a", "b"], 100)
# print(d)

# d = {"a": 1, "b": 2, "c": 3}
# d2 = [('r', 7), ('q', 9)]
# # d2 = {"r": 7, "q": 9}
# # print(list(d2.items()))
# # d.update(d2)  # своего рода сложение
# # d3 = d.copy()
# # d3.update(d2)
# # d3 = d | d2
# # print(d3)
# d |= d2
# print(d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
#
# print(d)
# print(new_d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# print(d)
# d["location"] = d.pop("city")
# print(d)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# # new_d = {value: key for key, value in d.items()}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(new_d)

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 2356, "S": 1257, "E": 3689, "W": 2585},
#     "Fiona": {"N": 8965, "S": 1065, "E": 7698, "W": 3542}
# }
# print(sales)
# for x in sales:
#     print(x)
#


# 24/02/2024
# d = {
#     "emp1": {"name": "John", "salary":  7500},
#     "emp2": {"name": "Emma", "salary":  8000},
#     "emp3": {"name": "Brad", "salary":  6500},
# }
# print(d["emp3"])
# print(d["emp3"]["salary"])
# d["emp3"]["salary"] = 8500
# 1 вариант
# for i in d:
#     print(i)
#     for j in d[i]:
#         print("\t", j, ":", d[i][j])

# 2 вариант
# for i in d:
#     print(i)
#     for j, v in d[i].items():
#         print("\t", j, ":", v)

# 24/02/2024 zip
# a = ("Dec", "Jan", "Feb")
# b = (12, 1, 2)
# c = [2.9, 3.7, 9.2]
# # d = dict(zip(a, b))
# # d = dict(zip(b, a))
# # d = list(zip(b, a, c))
# d = set(zip(b, a, c))
# print(d)

# one = {"name": "Igor", "surname": "Doe", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Smith", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# lt = [('Dec', 12), ('Jan', 1), ('Feb', 2)]
# a, b = zip(*lt)
# print(a)
# print(b)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# first = {"one": 1, "two": 2}
# second = {"three": 3, "four": 4}
# print({**first, **second})  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}, ** для словаря
# for k, v in {**first, **second}.items():
#     print(k, "=>", v)

# colors = ["red", "green", "blue"]
# i = 0
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
# for num, val in enumerate(colors, start=1):
#     print(num, ") ", val, sep="")

# studs = {}
# n = int(input("Кол-во студентов: "))
# # s = 0
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[name] = point
#     # s += point
# s = sum(studs.values())  # values когда словарь, за пределами цикла
# avg = s / n
# print(studs)
# print(s)
# print("Средний балл:", avg)
#
# for i in studs:
#     if studs[i] > avg:
#         print(i)
#
# for k, v in studs.items():
#     if v > avg:
#         print(k)


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, 8, "abc"))
# print(func())

# def summa(*params):
#     print(params)
#     print(*params)
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3))
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def ch(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 6, 7, 8, "abc"))

# def print_scores(student, *scores):
#     print("Student name:", student, end=", Оценки: ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jonathan", 100, 95, 88, 92, 99, 84)
# print_scores("Rick", 96, 20, 33, 66)

# def func(**kwargs):  # * кортеж, ** словарь
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(one="один"))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Wood", email="igor@mail.ru", country="Russia", age=22, phone=987654321)

# def func(a, b, *args, y=0, x=9, **kwargs):
#     return a, b, args, kwargs, y, x
#
#
# print(func(5, 1, 2, 3, 4, 5, 6, 7, y=100, n=9, m=10, x=5))
#
# my_dict = {"one": "first"}
# #
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# print("my_dict =", my_dict)
# db(k1=22, k2=31, k3=11, k4=91)
# print("my_dict =", my_dict)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print("my_dict =", my_dict)


# name = "Tom"  # Глобальная
# surname = ""
#
# def hi():
#     global name, surname  # перезаписали глобальную переменную name
#     name = "Sam"
#     surname = "Johnson"  # локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)
# print(surname)

# sum = 5
#
# lst = [9, 8, 7, 6, 5]
# print(sum(lst))

# 02/03/2024

# def add(a):
#     x = 2
#
#     def outer():
#         x = 3
#         print("x =", x)
#         return a + x
#
#     return outer()
#
#
# print(add(5))


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#
#     inner()
#     print("a =", a)
#     t = a
#
#
# fn()
# c = x + t  # 25 + 35 = 55  # 25+35=60
# print(c)

# def fn1():
#     x = 25  # 2
#
#     def fn2():
#         x = 33  # 4 # перезаписан x = 55
#
#         def fn3():
#             nonlocal x
#             x = 55  # 6
#
#         fn3()  # 5
#         print("fn2.x", x)  # 7   # 33
#     fn2()  # 3
#     print("fn1.x", x)  # 8   # 25
#
#
# fn1()  # 1

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7}

# Замыкание - функция возвращает другую функцию, но не вызывает ее

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(6)
# print(item2(10))

# print(outer(7)(10))  обычно не используется


# def func(a):
#     return a * 2
#
#
# x = func(5)
# print(x)


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1  # a += 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()

# lambda - выражения

# print((lambda x, y: x + y)(1, 2))
# # print((lambda x, y: x + y)(10, 20))
#
#
# def func(x, y):
#     return x + y
#
#
# # func = lambda x, y: + y
# print(func(1, 2))


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
#
# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7, 8))
# print((lambda *args: args)(1, 2, 3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t("abc_"))

# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func = inc1(10)
# print(func(5))
#
#
# def inc2(n):
#     return lambda x: n + x
#
#
# func2 = inc2(10)
# print(func2(5))
#
# inc3 = (lambda n: (lambda x: n + x))
# func3 = inc3(10)
# print(func3(5))
#
# print((lambda n: (lambda x: n + x))(10)(5))
#
# print((lambda n: (lambda x: (lambda c: n + x + c)))(2)(4)(6))

# def func(i):
#     return i[1]
#
#
# d = {"a": 15, "c": 10, "b": 5}
# # lst = sorted(d.items(), key=lambda i: i[1])
# lst = list(d.items())
# # print(lst)
# # # lst.sort(reverse=True)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=func)
# print(lst)
# print(dict(lst))


# players = [
#     {"name": "Антон", "last_name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last_name": "Бодня", "rating": 10},
#     {"name": "Федор", "last_name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last_name": "Семенов", "rating": 6},
# ]
# res = sorted(players, key=lambda item: item["last_name"])
# print(res)
#
# res1 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res1)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[1](8, 3))
# print(a[0](8, 3))
# print(a[3](8, 3))
# print(a[2](8, 3))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
# d[6]()

# from math import pi
#
# area = {
#     "Circle": lambda radius: pi * radius * radius,
#     "Rectangle": lambda a, b: a * b,
#     "Trapezoid": lambda a, b, h: (a + b) * h / 2,
# }
# print("Площадь окружности:", area["Circle"](2))
# print("Площадь прямоугольника:", area["Rectangle"](10, 13))
# print("Площадь трапеции:", area["Trapezoid"](7, 5, 3))

# print((lambda a, b: a if a > b else b)(5, 10))
# print((lambda a, b: a if a > b else b)(15, 10))

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))
#
# def outer(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j  # s = s+i*j
#         return s
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# print("Вносим изменения")
# print("Данные переносим на GitHub")


# def mult(t):
# return t * 2


# lst = [2, 8, 12, -5, -10]

# lst2 = list(map(mult, lst))
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
# print(lst2)

# t = (2.88, 1.78, -100.55)
#
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = dict(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# t = ('abcd', 'abc', 'deft', 'on', 'ert')
#
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# # t2 = tuple(map(lambda s: s * 3, t))
# # t2 = tuple(filter(lambda s: len(s) != 3, t))
# print(t2)

# b = [60, 90, 73, 85, 75, 99, 45, 71]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# from random import randint
#
# lst = [randint(1,40) for i in range(10)]
# print(lst)
#
# lst2 = list(filter(lambda t: 10 <= t <= 20, lst))
# print(lst2)


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))  # 1 - range, 2 - filter, 3 - map, 4 - list
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)

# Декораторы

# def hello():  # 3 func
#     return "hello, I am func 'hello'"
#
#
# def super_func(func):  # 2 в func приходит функция hello (нужно называть другим именем)
#     print("hello, I am super_func 'hello'")
#     print(func())
#
#
# super_func(hello)  # 1

# def hello():
#     return "hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def inner():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return inner
#
#
# def func_test():
#     print("hello, I am func_test 'hello'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print("*" * 40)
#         func()
#         print("=" * 40)
#
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("hello, I am func_test 'hello'")
#
#
# @my_decorator
# def hello():
#     print("hello, I am func 'hello'")
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные: ", arg1, arg2)
#         fn(arg1, arg2)
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# print_full_name("Ирина", "Ветрова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args: ", args)  # кортеж
#         print("kwargs: ", kwargs)  # словарь
#         fn(*args, **kwargs)
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):  # это функция декорирующая
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# @decor("Произведение:", "*")
# def mul(a, b):
#     print(a * b)
#
#
# summa(5, 2)
# sub(5, 2)
# mul(5, 2)

# def multiply(arg):
#     def decor(fn):
#         def wrap(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return wrap
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# Домашняя работа
# def wrap(fn)


# 17/03/2024
# Строки

# print(01)  # 0 стоять по умолчанию не может
# print(bin(18))  # 0b10010 - 0b - двоичная система
# print(oct(18))  # 0o22 - 0o - показатель, что восьмиричная система
# print(hex(18))  # 0x12 - 0x - показатель, что шестнадцатеричная система
#
# print(0b10010)
# print(0x12 + 0x12)
# print(0b10010 + 0o22)

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print("y" in e)
# # print(e[1])
# # print(e[-1])
# # print(e[1:4])
# # e[3] = 't'  # нельзя изменить буквы, строки не изменяемый тип данных
# e = e[:3] + "t" + e[4:]
# print(e)

# print("Привет")
# print(u"Привет")
# print(r"Привет")

# print('C:\\folder\\file.txt')
# print(r'C:\folder\file.txt')  # r - игнорирует \\
# print(r'C:\folder\\'[:-1])
# print(r'C:\folder' + "\\")
# print('C:\\folder\\')

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# a = f"Меня зовут {name}. Мне {age} лет."
# # print(f"Меня зовут {name}. Мне {age} лет.")
# print(a)
# print(f'Число {round(10.2564, 2)}, {5 + 3}')
# print(f'Число {12.526:.2f}')

# x = 10
# y = 5
# print(f'{x=}, {y=}')
# print(f'{x} x {y} / 2 = {x * y / 2}')

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + '\\' + file_name)

# s = '''Строка
# символов'''
# print(s)
#
# s1 = """Строка
# символов"""
# print(s1)
#
# s2 = 'Строка ' \
#       'символов'
# print(s2)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)

# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(sum.__doc__)
# print(len.__doc__)
# print(int.__doc__)
# print(type.__doc__)

# print(ord('a'))
# print(ord('и'))

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# 23/03/2024

# a = 97
# b = 122
# # if a > b:
# #     for i in range(b, a + 1):
# #         print(chr(i), end=" ")
# # else:
# #     for i in range(a, b + 1):
# #         print(chr(i), end=" ")
# if b > a
# for i in range(b, a + 1):
#     print(chr(i), end=" ")
#
# print('apple' == 'Apple')
# print('azple' > 'Apple')

# from random import randint
#
# min_ascii = 33
# max_ascii = 126
# shortest = 6
# longest = 16


# def random_password():
#     res = ''
#     for i in range(6)
#         res += randint(min_ascii, max_ascii):
#     return res
#
# print("Ваш случайный пароль: ", random_password())

# методы строк

# s = "hello, WORLD! I am learning Python."
# print(s)
# a = s.capitalize()
# print(a)
# print(s.lower())
# print(s.upper())
# print(s.count('h', 0, -4))
# print(s.find("Python"))  # поиск подстроки в строке, возвращает индекс совпадения, если совпадения нет вернет -1
# print(s.index("Python"))  # идентичен предыдущему, возвращает ValueError
# print(s.find("h", 1, -4))
# print(s.rfind("h"))
# print(s.rindex("h"))

# st = input("Введите два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# # print(first)
# # print(second)
# print(second + " " + first)

# s = "hello, WORLD! I am learning Python."
# print(s)
# print(s.endswith("on."))  # заканчивается ли строка на заданную подстроку (True, False)
# print(s.startswith("I am", 14))  # начинается ли строка с заданной подстроки (True, False)
# print(s.find("I am"))

# a = input("Введите число: ")
# try:
#     a = int(a)
#     print(a ** 2)
# except ValueError:
#     print("нужно ввести число")

# print("123".isdigit())  # состоит ли строка только из чисел
# print("12a3".isdigit())
#
# a = input("Введите число: ")
# b = 2
# if a.isdigit():
#     a = int(a)
#     print(a + b)
# else:
#     # print("нужно ввести число")
#     print(a + str(b))

# print("abc123".isalnum())  # состоит ли строка только из букв и чисел
# print("ABCabc".isalpha())  # состоит ли строка только из букв

# print("abc".islower())  # состоит ли строка только из букв в нижнем регистре, на спецзнаки не реагирует
# print("ANBN".isupper())  # состоит ли строка только из букв в верхнем регистре, на спецзнаки не реагирует

# print("py".center(10))
# print("py".center(10, "-"))

# print("    py".lstrip())
# print("py    ".rstrip())
# print("     py    ".strip())
# print("https://www.python.org".lstrip("/:pths"))
# print("https://www.python.orgw".strip("/:pthsw"))
# print("https://www.python.orgw".lstrip("/:pths").rstrip("w"))

# s = "hello, Python! I am learning Python. Python"
# print(s.replace("Python", "Java", 2))  # поиск и замена

# s = "-"
# seg = ("a", "b", "c")
# print(s.join(seg))  # s - выступает как символ объединитель
# print("..".join(["1", "2"]))  # join - объединяет (только строки) итерируемый объект в строку через символ разделитель
# print(":".join("Hello"))

# print("a b c".split())
# print("www.python.org".split(".", 1))
# print("www.python.org".rsplit(".", 1))

# Регулярные выражения

# import re

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список содержащий все совпадения с шаблона
# print(re.search(reg, s))  # возвращает первое совпадение с шаблона
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# # print(re.match(reg, s))  # поиск по шаблону только в начале строки
# print(re.split(reg, s, 3))  # возвращает список в котором строка разбита по шаблону
# print(re.sub(reg, "!", s, 1))  # поиск и замена

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765"
# # reg = r"[2024]"
# # reg = r"[0-9]"
# # reg = r"[а-я]"
# reg = r"[А-Яа-яё]"
# print(re.findall(reg, s))  # В папке 17. набор изображений
# print(ord("А"))
# print(ord("Я"))
# print(ord("а"))
# print(ord("я"))
# print(ord("ё"))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, st))

# st = "autor=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # pattern = r"\w+\s*=\s*[\w\s.]+"
# pattern = r"\w+\s*=\s*[^;,]+"
# print(re.findall(pattern, st))

# s1 = "12 сентября 2024 года 4567897"
# reg1 = r"\d{1,4}"
# print(re.findall(reg1, s1))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+\.$"
# print(re.findall(reg, s))


# def valid_login(name):
#     return re.findall("^[A-Za-z0-9_-]{3,16}$", name)
#
#
# print(valid_login("Python_master"))
# print(valid_login("Python"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello World"
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))

# text = """
# one # комментарий
# two
# """
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # per
# @         # @
# [a-z.-]+  # part 2
# """, "test@mail.ru", re.VERBOSE))

# 30/03/2024

# text = """Phyton,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# s1 = "12 сентября 2024 года 4567897"
# # reg1 = r"\d{2,4}"
# reg1 = r"\d{2}"
# print(re.findall(reg1, s1))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = r"Ольга|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"\w+\s*=\s*[.\w+]*"
# # reg = r"int\s*=\s*[.\w+]*|float\s*=\s*[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*[.\w+]*" # (?:...) - обозначает, что эта группирующая скобка является не сохраняюще
# reg = r"((?:int|float)\s*=\s*(?:[.\w+]*))"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# a = "31-08-2021"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19\d\d|20[0-9][0-9])"
# print(re.findall(pattern, a))
# print(re.search(pattern, a).group(1))
# m = re.search(pattern, a)
# print(m[0])  # это общее совпадение
# print(m[1])  # дата
# print(m[2])  # месяц
# print(m[3])  # год

# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# Функция. Рекурсия - должен быть базовый случай.

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # стек - область памяти в компьютере (5)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst [0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst [0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(354, 10))

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# names = ['Adam', ['Bob', ['Chat', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], "Ann"]
# print(names)
# print(len(names))
# # print(isinstance(names, list))
# # print(isinstance(names[0], list))
# # print(isinstance(names[1][0][0], list))
# print(count_items(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\nWorld "))

# 31/03/2024 (папка 19)

# f = open("file.txt", "r")
# # f = open(r"C:\Users\karip\OneDrive\Рабочий стол\Python\318\PY\Python1", "r")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()

# f = open("file.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open("file2.txt", "r")
# print(f.readline())
# print(f.readline(8))
# f.close()

# f = open("file2.txt", "r")
# # print(f.readlines(26))
# print("count =", len(f.readlines()))
# f.close()

# f = open("file2.txt", "r")
# for line in f:
#     print(line)
# f.close()

# f = open("file2.txt", "r")
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print("count =", count)

# f = open("xyz.txt", "w")  очищает и записывает
# f.write("Hello\nWorld")
# f.close()

# f = open("xyz.txt", "a")  # дозаписывает каждый раз
# f.write("\nNew text")
# f.close()

# line = ["This is line 1\n", "This is line 2\n"]
# f = open("xyz.txt", "w")
# f.writelines(line)
# f.close()

# lst = [i for i in range(1, 20)]
# print(lst)
#
# f = open("xyz.txt", "w")
# for index in lst:
#     f.write(str(index))
# f.close()
#
# f = open("xyz.txt", "r")
# d = f.read()
# print(d)
# f.close()

# lst = [i for i in range(1, 20)]
# print(lst)
#
# f = open("xyz.txt", "w")
# f.write("\t".join(map(str, lst)))
# f.close()
#
# f = open("xyz.txt", "r")
# d = f.read()
# st = list(map(int, d.split("\t")))
# print(st)
# f.close()

# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле:\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open(file, "r")
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello World!\n"
# print(read_line)
# f.close()
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()

# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле:\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open(file, "r")
# s = f.readlines()
# f.close()
# print(s)
#
# pos = int(input("pos = "))
# if 0 <= pos < len(s):
#     del s[pos]
# else:
#     print("Индекс введен не верно")
# print(s)
#
# f = open(file, "w")
# f.writelines(s)
# f.close()

# f = open("file.txt")
# print(f.read(3))
# print(f.tell())  # позиция, где находится курсор
# print(f.seek(1))  # перемещение курсора
# print(f.read())
# print(f.tell)
# f.close()


# f = open("file.txt", "r+")  режим r - не может создавать файл
# f.write("I am learning Python")
# print(f.seek(3))
# f.write("-new string-")
# f.close()

# f = open("file.txt", "a+")  # дополнительно записывает данные в конце, но считывать данные не может
# f.write("I am learning Python")
# print(f.seek(3))
# f.write("-new string-")
# f.close()

# with open("file.txt", "w") as f:
#     print(f.write("0123456789"))
# print(f.closed)

# with open("file.txt", "w") as f:
#     print(f.write("0123\n456\n789"))
#
# with open("file.txt", "r") as f:
#     for line in f:
#         print(line)

# def longest_words(file):
#     with open(file, "r", encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         print(max_length)
#         if len(res) == 1:
#             return res[0]
#         return max_length
#
#
# print(longest_words("file.txt"))

# one = "one.txt"
# two = "two.txt"
# three = "three.txt"
#
# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# # with open(one, "w") as f:
# #     f.write(text)
#
# with open(one, "r") as fr, open(two, "w") as fw:
#     for line in fw:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)
#
# one = "one.txt"
# two = "two.txt"
# three = "three.txt"
# #
# # with open(one, 'r') as f1:
# #     a = f1.read()
# #     print(a)
# #
# # with open(two, 'r') as f2:
# #     b = f2.read()
# #     print(b)
# #
# # c = a + b
# # print(c)
# #
# # with open(three, 'w') as f3:
# #     f3.write(c)
#
# with open(one, "r") as f1, open(two, "r") as f2, open(three, "w") as f3:
#     a = f1.readlines()
#     b = f2.readlines()
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     f3.writelines(c)
