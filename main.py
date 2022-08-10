x = int(input())
if x in range(0,17):
    print('Принадлежит')
else:
    print('Не принадлежит')

# Задача-2
x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Задача-3
x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Задача-4
num = int(input())
if 999 < num < 10000 and (num % 7 == 0 or num % 17 == 0):
    print("YES")
else:
    print("NO")

# Задача-5
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print("NO")

# Задача-6
# put your python code here
num = int(input())
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("YES")
else:
    print("NO")

# Задача-7
col, row, col_next, row_next = int(input()), int(input()), int(input()), int(input())
if col == col_next or row == row_next:
    print("YES")
else:
    print("NO")

# Задача-8
x, y, x1, y1 = int (input ()), int (input ()), int (input ()), int (input ())
if abs (x - x1) <= 1 and abs (y - y1) <= 1:
    print ("YES")
else:
    print ("NO")


# Задача-9

