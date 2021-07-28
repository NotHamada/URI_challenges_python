import math

values1 = input().split(" ")
values2 = input().split(" ")

x1, y1 = values1
x2, y2 = values2

result = math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)

print ('%.4f' % result)