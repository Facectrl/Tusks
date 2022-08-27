# put your python code here
a, b, c = int(input()), int(input()), int(input())
if a == b and a == c:
    print("Равносторонний")
elif a == b and a != c or a != b and a == c or a != b and b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")


# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число
a, b, c = int(input()), int(input()), int(input())
if a < b < c:
    print(b)
elif a > b > c:
    print(b)
elif a > c > b:
    print(c)
elif a < c < b:
    print(c)
else:
    print(a)


a, b, c = int(input()), int(input()), int(input())
if c > a:  # сортировка по возрастанию методом простого выбора (по возрастанию) и потом поиск медианы
    a, c = c, a
if b > a:
    a, b = b, a
if c > b:
    b, c = c, b
print(a, b, c)



# Дан порядковый номер месяца . Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.
m = int(input())
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 12 or m == 10:
    print('31')
elif m == 6 or m == 4 or m == 11 or m == 9:
    print('30')
else:
    print("28")


weight = int(input())
if weight < 60:
    print("Легкий вес")
elif 60 <= weight < 64:
    print("Первый полусредний вес")
elif 64 <= weight < 69:
    print("Полусредний вес")