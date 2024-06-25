import math
a, b = map(int, input().split())
print((int(b * math.log(a, 10)) + 1))