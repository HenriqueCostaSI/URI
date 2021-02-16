import math

a, b, c  = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

y = (a + b + abs(a - b))/2

x = (y + c + abs(y - c))/2

print(f'{int(x)} eh o maior')
