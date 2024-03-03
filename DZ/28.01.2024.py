a = [int(input("-> ")) for i in range(int(input("Введите кол-во элементов списка: \n n = ")))]
k = int(input("Введите индекс: \n k = "))
for i in range(len(a)):
    if i == k:
        if i < len(a):
            a.pop(i)
print(a)
