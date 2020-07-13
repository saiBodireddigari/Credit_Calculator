# put your python code here
import math

side1 = int(input())
side2 = int(input())
side3 = int(input())

p = (side1 + side2 + side3) / 2  # half perimeter

area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

print(area)
