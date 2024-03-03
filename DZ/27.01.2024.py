k = int(input("Введите количество символов: "))
t = input("Тип символа: ")
a = int(input("0 - горизонтальная \n 1 - вертикальная \n Укажите ориентацию линии: "))

# if a == 0:
#     for i in range(k):
#         for e in range(a):
#             print(t, end=" ")
#         print()
# elif a == 1:
#     for i in range(k):
#         for e in range(a):
#             print(t, end="\n")
i = 0
while i < k:
    if a == 0:
        print(t, end=" ")
    if a == 1:
        print(t)
    i += 1
else:
    print("Такой ориентации не предусмотрено")





# if a == 0:
#     print(t * k, end=" ")
# elif a == 1:
#     for i in range(k):
#         print(t)
# else:
#     print("Неверный выбор ориентации линии.")