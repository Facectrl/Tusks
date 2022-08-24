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
