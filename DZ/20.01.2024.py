# n = int(input("Введите пятизначное число: "))
# m = 1
# s = 0
# count = 0
#
# while n > 0:
#     s += n % 10
#     m *= n % 10
#     n = n // 10
#     count += 1
# sum_ = s // count
# print("Произведение всех цифр пятизначного числа равно", m)
# print("Среднее арифметическое  всех цифр пятизначного числа равно", sum_)

n = int(input("Введите пятизначное число: "))
n1 = n % 10
n = n // 10
n2 = n % 10
n = n // 10
n3 = n % 10
n = n // 10
n4 = n % 10
n = n // 10
n5 = n % 10
n = n // 10
mult = n1 * n2 * n3 * n4 * n5
summa = (n1 + n2 + n3 + n4 + n5) // 5
print("Произведение всех цифр пятизначного числа равно: ", mult)
print("Среднее арифметическое  всех цифр пятизначного числа равно", summa)





