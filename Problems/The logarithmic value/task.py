import math

a = int(input())
b = int(input())

if b <= 1:
    c = math.log(a)
    print(round(c, 2))
else:
    c = math.log(a, b)
    print(round(c, 2))
