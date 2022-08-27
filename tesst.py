"""""
n, k = int(input()), int(input())
if n > k:
    print("NO")
elif k > n:
    print('YES')
elif n == k:
    print("Don't know")
"""

a, b, c = int(input()), int(input()), int(input())
if a == b and b == c:
    print("Равносторонний")
elif a == b:
    if b != c:
        print("Равнобедренный")
elif a != b:
    if a == c:
        print("Равнобедренный")
    elif b == c:
        print("Равнобедренный")
else:
    print("Разносторонний")

"""