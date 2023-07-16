N = int(input())
x = []
y = []
for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

x1 = min(x)
x2 = max(x)
y1 = min(y)
y2 = max(y)

print((x2-x1)*(y2-y1))