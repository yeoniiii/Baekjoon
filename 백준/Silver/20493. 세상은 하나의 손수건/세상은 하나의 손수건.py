import sys
input = lambda: sys.stdin.readline().rstrip()

def move(dist):
    global d, x, y

    if d == 0:
        x += dist
    elif d == 1:
        y -= dist
    elif d == 2:
        x -= dist
    elif d == 3:
        y += dist
    
    return x, y


N, T = map(int, input().split())
x, y, d = 0, 0, 0
dist = 0

for n in range(N):
    Ti, Si = input().split()

    x, y = move(int(Ti) - dist)
    dist = int(Ti)

    if Si == 'right':
        if d == 3:
            d = 0
        else:
            d += 1
    elif Si == 'left':
        if d == 0:
            d = 3
        else:
            d -= 1
    
x, y = move(T - dist)

print(x, y)