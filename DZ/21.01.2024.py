n = int(input("Введите число от 1 до 99: "))

if 1 <= n <= 99:
    if n % 10 == 1:
        print(n, "копейка")
    elif 2 <= n % 10 <= 4:
        print(n, "копейки")
    elif 5 <= n <= 20:
        print(n, "копеек")
    else:
        print(n, "копеек")
else:
    print(n, "Не верное число!")



