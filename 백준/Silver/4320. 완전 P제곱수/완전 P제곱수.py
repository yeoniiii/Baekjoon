import sys
input = lambda: sys.stdin.readline().rstrip()
import math

while True:
    x = int(input())
    if x == 0:
        break

    p = 1
    sqrt = int(math.sqrt(abs(x))) + 1
    find = False

    if x > 0:
        for i in range(2, sqrt+1):
            for j in range(2, 31):
                temp = math.pow(i, j)
                if temp > x:
                    break
                elif temp == x:
                    p = j
                    find = True
                    break
            if find:
                break
                    
    else:
        for i in range(-2, -sqrt-1, -1):
            for j in range(3, 32, 2):
                temp = math.pow(i, j)
                if temp < x:
                    break
                elif temp == x:
                    p = j
                    find = True
                    break
            if find:
                break
    
    print(p)