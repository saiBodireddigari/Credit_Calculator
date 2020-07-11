import math

degrees = int(input())

radians = degrees * (math.pi / 180)
tan = math.tan(radians)

print(round(1 / tan, 10))