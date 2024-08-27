x1, y1, x2, y2, x3, y3 = map(int, input().split())

def calculate_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

d12 = calculate_distance(x1, y1, x2, y2)
d23 = calculate_distance(x2, y2, x3, y3)
d31 = calculate_distance(x3, y3, x1, y1)

d = [d12, d23, d31]
d.sort()

if (x1-x2)*(y1-y3)==(x1-x3)*(y1-y2):
    print(-1.0)
else:
    print((d[2]-d[0])*2)